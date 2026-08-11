import cv2
import os

# Настройки
frame_dir = r"Ваш путь до папки с кадрами"
cfg_dir = r"Ваш путь до папки с cfg"
scale = 0.1
pitch_const = 0
yaw_const = 90
max = 250  # Лимит команд на один конфиг

if not os.path.exists(cfg_dir): os.makedirs(cfg_dir)

frame_idx = 0

while True:
    img_path = os.path.join(frame_dir, f"Frame_{frame_idx:04d}.jpg")
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
                pitch = pitch_const + (y - 240) * scale
                yaw = yaw_const - (x - 320) * scale
                commands.append(f"setang {pitch:.2f} {yaw:.2f}; +attack; -attack;")
        
        commands.append("setang 0 90;")

       
        if len(commands) <= max:
            cfg_path = os.path.join(CFG_DIR, f"Frame_{frame_idx:04d}.cfg")
            with open(cfg_path, "w", encoding="utf-8") as f:
                f.write("\n".join(commands))
            print(f"Frame {frame_idx} created: {len(commands)} cmds")
            break
        
        conf += 0.005 # Сильнее упрощаем геометрию, если не влезли в лимит

    frame_idx += 1
