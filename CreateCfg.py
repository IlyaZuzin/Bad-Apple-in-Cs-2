import cv2
import os

# Настройки
FRAME_DIR = r"G:\Python\Bad Apple cs 2\Frames"
CFG_DIR = r"G:\Python\Bad Apple cs 2\Cfg"
SCALE = 0.1
CENTER_PITCH = 0
CENTER_YAW = 90
MAX_COMMANDS = 250  # Лимит команд на один конфиг

if not os.path.exists(CFG_DIR): os.makedirs(CFG_DIR)

frame_idx = 0

while True:
    img_path = os.path.join(FRAME_DIR, f"Frame_{frame_idx:04d}.jpg")
    img = cv2.imread(img_path)
    if img is None: break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    conf = 0.3
    while True:
        commands = [
            "setpos 59.183067 -1622.782715 -106.411316;",
            "setang 0 90;"
        ]
        
        for cnt in contours:
            approx = cv2.approxPolyDP(cnt, conf, True)
            for point in approx:
                x, y = point[0]
                pitch = CENTER_PITCH + (y - 240) * SCALE
                yaw = CENTER_YAW - (x - 320) * SCALE
                commands.append(f"setang {pitch:.2f} {yaw:.2f}; +attack; -attack;")
        
        commands.append("setang 0 90;")

        # Проверка лимита: если команд слишком много, упрощаем контуры
        if len(commands) <= MAX_COMMANDS:
            cfg_path = os.path.join(CFG_DIR, f"Frame_{frame_idx:04d}.cfg")
            with open(cfg_path, "w", encoding="utf-8") as f:
                f.write("\n".join(commands))
            print(f"Frame {frame_idx} created: {len(commands)} cmds")
            break
        
        conf += 0.005 # Сильнее упрощаем геометрию, если не влезли в лимит

    frame_idx += 1