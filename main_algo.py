from tensorflow.keras.models import load_model
import cv2


class Main:
    def __init__(self):
        self.model=load_model('model.h5')
    
    def pred(self,img):
        re=self.model.predict(img)
        age=round(re[1][0][0])
        gender=round(re[0][0][0])
        print(re)
        return age,gender
    

    def start(self,img):
        face = img
        #face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
        face = cv2.resize(face,(32,32))
        face = face.reshape((1,32,32,3))
        age,gender=self.pred(face);
        return age,gender
    
    def detect_face(self,img):
        face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            face=img[y:y+h,x:x+w]
        return face
    


# def pred(img,model):
#     re=model.predict(img)
#     age=round(re[1][0][0])
#     gender=round(re[0][0][0])
#     print(re)
#     return age,gender
#     
# 
# def start(folder):
#     model=load_model('model.h5')
#     age=[]
#     gender=[]
#     
#     for photo in os.listdir(folder):
#         face = cv2.imread(folder+photo)
#         #face = cv2.cvtColor(face,cv2.COLOR_BGR2RGB)
#         face = cv2.resize(face,(32,32))
#         face = face.reshape((1,32,32,3))
#         re_age,re_gender=pred(face,model)
#         age.append(re_age)
#         gender.append(re_gender)
#     return max(age,key=age.count),max(gender,key=gender.count)
#         
#     


#f=Main()

#img=cv2.imread('IMG_20191018_124953.jpg')

#faces=f.detect_face(img)

#faces

#for (x,y,w,h) in faces:
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#cv2.imshow('IMG_20191018_121312.jpg',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

#age,gender=f.start(faces)

#age

