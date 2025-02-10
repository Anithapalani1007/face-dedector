#web camera
import cv2

#trained dataset
trainedDataset= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video=cv2.VideoCapture('videos/VID_44280831_003314_239.mp4')
while True:
    success,frame=video.read()
    #succes,frame=video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_image)
        print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video',frame)
        cv2.waitKey(1)
    else:
        print("video completed or frame Nil")
        break

      #img
  import cv2

#trained dataset
trainedDataset= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#read a image
img=cv2.imread('images/download (1).jpg')

#  convert into grayscale

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=trainedDataset.detectMultiScale(gray)
print(faces)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
cv2.imshow('ani',img)
#cv2.imshow('gray',gray)
cv2.waitKey()

#upload video
import cv2

#trained dataset
trainedDataset= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
video=cv2.VideoCapture('videos/VID_44280831_003314_239.mp4')
while True:
    success,frame=video.read()
    #succes,frame=video.read()
    if success==True:
        gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = trainedDataset.detectMultiScale(gray_image)
        print(faces)
        for x, y, w, h in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.imshow('video',frame)
        cv2.waitKey(1)
    else:
        print("video completed or frame Nil")
        break

      
