from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os

# Folder containing the videos, with no matter if they're located in subdirectories
generalpath ="/home/lx/Desktop/videos"

# Creating the name, paths and full names (path+name) of each video & storing in a arrays
listnames=[]
listpath=[]
fullpath=[]
for roots, divs, files in os.walk(generalpath):
   for file in files:
      if(file.endswith(".mp4")):
         listnames.append(os.path.join(file))  #roots,file
         listpath.append(os.path.join(roots))
         fullpath.append(os.path.join(roots,file))

# print(listnames)
# print(listpath)
# Editing the video, trim the 9 first seconds of every video and store them appending the string 'a' on every
# video's name. Every video is created inside the folder of the original video

for i in range(len(listnames)):
   clip = VideoFileClip(fullpath[i])
   newclip = clip.subclip(9.25,clip.duration)
   newclip.write_videofile(listpath[i]+'/a'+listnames[i])

# Run with python3 Trimclip.py


