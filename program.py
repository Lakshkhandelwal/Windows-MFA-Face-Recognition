import cv2
import numpy as np
import os
from PIL import Image
import time
import ctypes
import shutil

def main():
    print("Option 1 : Capture Your Face")
    print("Option 2 : Train program to detect faces")
    print("Option 3 : Start Windows Lock")
    print("Option 4 : Reset the Program")
    print("Option 5 : Exit from the Program")
    choice = int(input("Enter your option: "))
    if choice == 1:
        create()
    elif choice == 2:
        train()
    elif choice == 3:
        detect()
    elif choice == 4:
        try:
            shutil.rmtree("dataSet")
            shutil.rmtree("recognizer")
            print("\nAll the files have been deleted & program reset complete! \n\n")
        except OSError as e:
            print("Error: %s : %s" % (dir_path, e.strerror))
        main()
    elif choice == 5:
        exit()
    else:
        print("\nIncorrect Option Selected, Choose Correct Options\n\n")
        main()

def create():
    if not os.path.isdir("dataSet"):
        os.mkdir("dataSet")
    if not os.path.isfile("haarcascade_frontalface_default.xml"):
        print("Cascade Classifier File Not Found")
        main()
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0);
    id=int(input('Enter user id: '))
    sampleNum=0
    while(True):
        ret,img = cam.read();
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5);
        for (x,y,w,h) in faces:
            sampleNum=sampleNum+1
            cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
            cv2.waitKey(100);
        cv2.imshow("Face",img);
        cv2.waitKey(1);
        if(sampleNum>20):
            break
    cam.release()
    cv2.destroyAllWindows()
    main()


def train():
    if not os.path.isdir("recognizer"):
        os.mkdir("recognizer")
    if not os.path.isdir("dataSet"):
        print("No capture faces found, run the option 1 again !!!!!!!")
        main()
    if len(os.listdir("dataSet")) == 0:
        print("No capture faces found, run the option 1 again !!!!!!!")
        main()
    recognizer = cv2.createLBPHFaceRecognizer();
    path ='dataSet'
    def getImagesWithID(path):
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
        faces=[]
        IDs=[]
        for imagePath in imagePaths:
            faceImg=Image.open(imagePath).convert('L');
            faceNp=np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            cv2.imshow("training",faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces
    Ids,faces=getImagesWithID(path)
    recognizer.train(faces,Ids)
    recognizer.save('recognizer/trainingData.yml')
    cv2.destroyAllWindows()
    main()


def detect():
    if not os.path.isfile("haarcascade_frontalface_default.xml"):
        print("Cascade Classifier File Not Found")
        main()
    if not os.path.isfile("recognizer\\trainingData.yml"):
        print("Training Data File Not Found")
        main()
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
    cam = cv2.VideoCapture(0);
    rec = cv2.createLBPHFaceRecognizer();
    rec.load('recognizer\\trainingData.yml')
    id=0
    font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
    def funct():
        while(True):
            ret,img = cam.read();
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = faceDetect.detectMultiScale(gray,1.3,5);
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])                   
                cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
                cv2.imshow("Face",img);
                cv2.waitKey(1)
                return 'True'
            cv2.imshow("Face",img);
            cv2.waitKey(1)
            return 'False'
    while(True):
        value = funct()
        if value == 'True':
            pass
        else:
            t_end = time.time() + 5
            listr=[]
            while time.time() < t_end:
                listr.append(funct())
            check2='false'
            for x in listr:
                if x == 'True':
                    check2='true'
            if check2=='false':
                ctypes.windll.user32.LockWorkStation()
            else:
                pass
    cam.release()
    cv2.destroyAllWindows()
    main()
        
main()
        
