from moviepy.editor import VideoFileClip
from moviepy.editor import *
import os

# Folder containing the videos, with no matter if they're located in subdirectories
generalpath ="/home/lx/Desktop/videos"

# Creating the name, path and full name (path+name) of each video and storing in arrays
listnames=[]
listpath=[]
fullpath=[]
for roots, divs, files in os.walk(generalpath):
   for file in files:
      if(file.endswith(".mp4")):
         listnames.append(os.path.join(file))          #roots & files for mp4
         listpath.append(os.path.join(roots))
         fullpath.append(os.path.join(roots,file))

newname=[]
newpathfolder=[]
for i in range(len(listnames)):
   clip = VideoFileClip(fullpath[i])
   newclip = clip.subclip(9.25,clip.duration)
   newname.append(listnames[i][listnames[i].find('.'):])  # Deletes the numbering
   #newclip.write_videofile(listpath[i]+'/a'+str(i+1)+newname[i])
   newpathfolder.append(listpath[i].replace("/videos/","/videos1/")) # creating the new folders
   os.makedirs(newpathfolder[i])                          
   newclip.write_videofile(newpathfolder[i]+'/'+str(i+1)+newname[i])

