import cv2
import os
import re
from moviepy import VideoFileClip, AudioFileClip

# 1. Настройки
image_folder = r"G:\Python\Bad Apple cs 2\Screenshot"
temp_video = r"G:\Python\Bad Apple cs 2\temp_no_audio.mp4"
final_video = r"G:\Python\Bad Apple cs 2\final_bad_apple.mp4"
source_video_with_audio = r"G:\Python\Bad Apple cs 2\test_audio.mp3" # Файл, откуда берем звук
fps = 30

# 2. Сборка видео из скриншотов
images = [img for img in os.listdir(image_folder) if img.endswith((".png", ".jpg", ".jpeg"))]
# Сортировка файлов по числам в названии
images.sort(key=lambda f: int(re.sub(r'\D', '', f)))

if not images:
    print("Изображения не найдены!")
    exit()

# Определяем размер кадра по первому изображению
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

print("Собираем видео...")
for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

video.release()

# 3. Добавление звука через MoviePy
try:
    video_clip = VideoFileClip(temp_video)
    # Берем аудиодорожку из исходного видео
    audio_clip = AudioFileClip(source_video_with_audio)
    
    # Соединяем
    final_clip = video_clip.with_audio(audio_clip)
    final_clip.write_videofile(final_video, codec="libx264", audio_codec="aac")
    
    # Закрываем файлы и удаляем временный
    video_clip.close()
    audio_clip.close()
    if os.path.exists(temp_video):
        os.remove(temp_video)
    print(f"Готово! Файл сохранен как {final_video}")
except Exception as e:
    print(f"Ошибка при работе со звуком: {e}")