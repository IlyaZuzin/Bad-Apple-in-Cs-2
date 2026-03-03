from moviepy import VideoFileClip

# Укажите путь к вашему видео
video_path = r"G:\Python\Bad Apple cs 2\Bad_Apple.mp4"
output_audio_path = r"G:\Python\Bad Apple cs 2\test_audio.mp3"

# Загружаем видеофайл
video = VideoFileClip(video_path)

# Извлекаем аудио и сохраняем его
video.audio.write_audiofile(output_audio_path)

# Закрываем файл, чтобы освободить ресурсы
video.close()

print("Аудио успешно извлечено!")