from moviepy.editor import VideoFileClip
import shutil, os
from collections import Counter
import numpy as np
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Folder containing the videos, with no matter if they're located in subdirectories
generalpath ="/home/jo/Desktop/vix"

# Creating the name, path and full name (path+name) of each video & storing them in arrays
listnames=[]
listpath=[]
fullpath=[]

sublistnames=[]  # subtitles
sublistpath=[]   # subtitles
subfullpath=[]

for roots, divs, files in os.walk(generalpath):
   for file in files:
      if(file.endswith(".srt")):
         sublistnames.append(os.path.join(file))          #roots,file
         sublistpath.append(os.path.join(roots))
         subfullpath.append(os.path.join(roots,file))
         
for roots, divs, files in os.walk(generalpath):
   for file in files:   
      if(file.endswith(".mp4")):
         listnames.append(os.path.join(file))          #roots,file
         listpath.append(os.path.join(roots))
         fullpath.append(os.path.join(roots,file))


rootss, divss, filess = next(os.walk(generalpath))
#print(list(dict.fromkeys(divss)))

###############################################################
#print(divss)   # divss main directories ['1. directorio1', '2. directorio2', '3. directorio3']
print(subfullpath[2])
print(sublistpath[2]) #/home/lx/Desktop/vid/2. directorio2
indexfold=int(sublistpath[2].split('/vix/')[1].split('.')[0]) # index of the folder
print(indexfold) # ouput fold index 2
###############################################################


############################################################### 
##########   Print(numberfiles) # totalfiles inside each folder 
numberfiles = []
for k in range(len(divss)):
   newpa=generalpath +'/'+ divss[k]
   rooth, divh, fileh = next(os.walk(newpa))
   numberfiles.append(int(len(fileh)/2))  #divde betwen 2, video and srt
############################################################### 


############################################################### 
diction1=dict(zip(divss, numberfiles))
#     print(diction1)

##########  Create array of index folders  ########## 
numberdirs = []
for k in range(len(divss)):
   #newpa=generalpath +'/'+ divss[k]
   rootg, divg, fileg = next(os.walk(generalpath))
   numberdirs.append(int(divg[k].split(".")[0]))
   
print(numberdirs)
diction2=dict(zip(numberdirs, numberfiles))  # 2. Dir has 4 == diction2={2:4,..
print(diction2) 
###############################################################  

###############################################################  
suma = 0
newva  = []
for i in range(indexfold-1):
   if(diction2.get(i+1)==None):
      a = 0
   else:
      a = diction2.get(i+1)
   suma = suma + a
   #suma = suma + diction2.get(i+1)
   #newva.append(diction2.get(i+1))
#print(suma)
print(suma)
###############################################################  

#print(listpath[0].replace("/vip/","/vip1/"))

print(sublistnames[0])
print(sublistnames[0][sublistnames[0].find('.'):]) #
print(sublistnames[0].split('.')[0])  # extract index of the file

print(int(sublistnames[0].split('.')[0])+100)

print(sublistpath[0])
#"""

newname=[]
newpathfolder=[]
subnewname=[]
subnewpathfolder=[]
inddexfile=[]
sinddexfile=[]


###############################################################
############## CREATING THE FOLDERS  #######################
newlistpathsim=list(dict.fromkeys(sublistpath))
#print()
for i in range(len(newlistpathsim)):
   os.makedirs(newlistpathsim[i].replace("/vix/","/vix1/"))
#"""
###############################################################    

#print(divss)
#newlist=list(dict.fromkeys(sublistpath))
for i in range(len(sublistnames)):
   clip = VideoFileClip(fullpath[i])
   subnewname.append(sublistnames[i][sublistnames[i].find('.'):])
   newname.append(listnames[i][listnames[i].find('.'):])
   subnewpathfolder.append(sublistpath[i].replace("/vix/","/vix1/")) # creating the new folders
   newpathfolder.append(listpath[i].replace("/vix/","/vix1/"))
   sinddexfile.append(int(sublistnames[i].split('.')[0]))
   inddexfile.append(int(listnames[i].split('.')[0]))
   indexfold=int(sublistpath[i].split('/vix/')[1].split('.')[0])
   suma = 0
   for k in range(indexfold-1):
      if(diction2.get(k+1)==None):
         a = 0
      else:
         a = diction2.get(k+1)
      suma = suma + a
   shutil.copy(subfullpath[i],subnewpathfolder[i]+"/"+str(suma+sinddexfile[i])+subnewname[i])
   ffmpeg_extract_subclip(fullpath[i],9.5,clip.duration, targetname=newpathfolder[i]+"/"+str(suma+inddexfile[i])+newname[i])

