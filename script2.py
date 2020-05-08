import cv2
import glob
#import file. saves as numpy array
class read_file:
    def __init__(self,filename):
        img=cv2.imread(filename,1) #0 - grayscale, 1- RGB
        self.img=img

    def resize(self,image):
        self.resize_image=cv2.resize(self.img,(100,100)) #img,tuple

    def show_image(self,image):
        cv2.imwrite("resize"+image,self.resize_image)
        cv2.imshow("My file",self.resize_image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()

images=glob.glob("*.jpg")
for image in images:

    file=read_file(image)
    file.resize(image)
    file.show_image(image)
