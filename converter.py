import os
from moviepy.editor import *
import sys

filename = sys.argv[1]
print(filename)
video = VideoFileClip(os.path.join(filename))
video.audio.write_audiofile(os.path.join(f"{filename}.mp3"))