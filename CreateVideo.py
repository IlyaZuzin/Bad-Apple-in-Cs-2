import cv2
import os
import re
from moviepy import VideoFileClip, AudioFileClip

image_folder = r"G:\Python\Bad Apple cs 2\Screenshot" # Папка со скриншотами
temp_video = r"G:\Python\Bad Apple cs 2\temp_no_audio.mp4" 
final_video = r"G:\Python\Bad Apple cs 2\final_bad_apple.mp4" # Конечный результат
source_video_with_audio = r"G:\Python\Bad Apple cs 2\test_audio.mp3" # Файл, откуда берем звук
fps = 30

images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
images.sort(key=lambda f: int(re.sub(r'\D', '', f))) # Незабудьте поменять название диска

if not images:
    print("Изображения не найдены!")
    exit()


frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

print("Собираем видео...")
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()

try:
    video_clip = VideoFileClip(temp_video)
    audio_clip = AudioFileClip(source_video_with_audio)

    final_clip = video_clip.with_audio(audio_clip)
    final_clip.write_videofile(final_video, codec="libx264", audio_codec="aac")

    video_clip.close()
    audio_clip.close()
    if os.path.exists(temp_video):
        os.remove(temp_video)
    print(f"Готово! Файл сохранен как {final_video}")
except Exception as e:
    print(f"Ошибка при работе со звуком: {e}")
