from moviepy import VideoFileClip

# Укажите путь к вашему видео
video_path = r"G:\Python\Bad Apple cs 2\Bad_Apple.mp4"
output_audio_path = r"G:\Python\Bad Apple cs 2\test_audio.mp3"

video = VideoFileClip(video_path)

video.audio.write_audiofile(output_audio_path)

video.close()

print("Аудио успешно извлечено!")
