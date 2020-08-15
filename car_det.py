#Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
#Type "help", "copyright", "credits" or "license()" for more information.
import cv2
#print(cv2.__version__)

    
cascade_src = "C:\\Users\\ASUS\\Downloads\\Vehicle detection\\mobil\\classifier\\cascade.xml"
video_src = "C:\\Users\ASUS\Downloads\Vehicle detection\\video4.mp4"
#video_src = 'dataset/video2.avi'

cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cascade = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cascade:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)      
    
    cv2.imshow('video', img)
    
    if cv2.waitKey(22) == 10:
        break

cv2.destroyAllWindows()

cap.release()
        
