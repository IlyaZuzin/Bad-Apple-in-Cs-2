import cv2
import os

video_path = r"G:\Python\Bad Apple cs 2\Bad_Apple.mp4"
output_dir = r"G:\Python\Bad Apple cs 2\Frames"


os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)


if not cap.isOpened():
    print("Ошибка: Не удалось открыть видео.")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_name = os.path.join(output_dir, f'Frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_name, frame)
    frame_count += 1
cap.release()


print(f"Готово! Сохранено кадров: {frame_count}")
