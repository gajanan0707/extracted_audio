from moviepy.editor import VideoFileClip

# Path to your video file
video_path = 'videos/example_video.mp4'

# Load the video file
video = VideoFileClip(video_path)

# Extract the audio
audio = video.audio

# Save the audio to a file
audio_path = 'audio/extracted_audio.mp3'
audio.write_audiofile(audio_path)

print(f"Audio extracted and saved to {audio_path}")