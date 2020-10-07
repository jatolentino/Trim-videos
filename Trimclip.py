from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os
generalpath ="/home/lx/Desktop/videos"
listnames=[]
listpath=[]
fullpath=[]
for roots, divs, files in os.walk(generalpath):
   for file in files:
      if(file.endswith(".mp4")):
         listnames.append(os.path.join(file))  #roots,file
         listpath.append(os.path.join(roots))
         fullpath.append(os.path.join(roots,file))

print(listnames)
print(listpath)

for i in range(len(listnames)):
   clip = VideoFileClip(fullpath[i])
   newclip = clip.subclip(9.25,clip.duration)
   newclip.write_videofile(listpath[i]+'/a'+listnames[i])


'''=[1,2]
for i in range(2):
   with open(listpath[i], 'w') as f:
      data = 'some data to be written to the file'
      f.write(data)
'''
