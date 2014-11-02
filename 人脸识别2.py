import numpy
import cv2
import os

def process(srcFile):
  face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt2.xml')
  img = cv2.imread(srcFile)
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.2, 1)
  for(x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
   # cv2.imshow('Rectangle an image', img)
  
  save_path= os.path.splitext(files)[0]+'_out.jpg'
  print 'save',save_path
  cv2.imwrite(save_path,img)
   # cv2.waitKey(0)
  #  cv2.destroyAllWindows()
# def getDir:
#   return os.path.split(os.path.realpath(__file__))[0]

if __name__ =="__main__":

  for files in os.listdir(os.getcwd()):
    if os.path.splitext(files)[1] == '.jpg' or '.JPG':
       print files
       process(files)

   
