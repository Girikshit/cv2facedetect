import threading
import sys

import cv2
from deepface import DeepFace
cap= cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)

count = 0
reference_img= cv2.imread("/home/stalk3r/Desktop/reference.jpg")

condition = threading.Condition()
event= threading.Event()
threads= []
face_match= False

def check_face(frame,condition,event):
    global face_match
    print("checkface entered")
    with condition:
        event.wait()
        print("thread started")
        try:
            if DeepFace.verify(frame, reference_img.copy())['verified']:
                face_match=True
                print('MAtched!!!!')
            else:
                face_match=False
                print('False face match')
        except ValueError:
            face_match=False
            print('Deepface value error')
        print('thread finished')


while(True):
    ret, frame= cap.read()

    #check faulty frame
    if frame is None:
        raise ValueError("Unable to get frame")
    
    if reference_img is None:
        print('Referenceimg is none')

    if ret:
        if count%60 == 0:
            if not any(thread.is_alive() for thrd in threads):
                try:
                    thread= threading.Thread(target= check_face, args=(frame.copy(),condition,event,))
                    thread.start()
                    print('Starting thread')
                    threads.append(thread)
                    event.clear()
                    
                except ValueError:
                    print("Error starting thread")
            else:
                print("Previous thread running.. skipping")
            event.set()
        count+=1

        if face_match:
            cv2.putText(frame,"Match",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,"NO Match",(20,450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),3)

        cv2.imshow("video",frame)
    else:
        print("unable to video capture")
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows() 