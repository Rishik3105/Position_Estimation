import cv2 as cv
import mediapipe as mp
import time

cap=cv.VideoCapture(0)
mppose=mp.solutions.pose
pose=mppose.Pose()
mpdraw=mp.solutions.drawing_utils
line_spec = mpdraw.DrawingSpec(color=(0, 255, 0), thickness=3)  
circle_spec = mpdraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=5)
ctime=0
ptime=0
while True:
    success,img=cap.read()
    imgRGB=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results=pose.process(imgRGB)
    if results.pose_landmarks:
        for id,lm in enumerate(results.pose_landmarks.landmark):
         h,w,c=img.shape
         cx,cy=int(lm.x*w),int(lm.y*h)
         print(f'Id number{id},{cx},{cy}')
         mpdraw.draw_landmarks(img,results.pose_landmarks,mppose.POSE_CONNECTIONS,circle_spec,line_spec)
    ctime=time.time()
    fps=1 /(ctime - ptime)
    ptime=ctime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_PLAIN,3,(255,255,0),3)
    cv.imshow("Image",img)
    if cv.waitKey(10) & 0xFF== ord('q'):
      break
