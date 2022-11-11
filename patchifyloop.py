import os
import cv2
from patchify import patchify

path ='C:/Users/images/'
files = os.listdir(path)
def makepatches():
    for item in files:
        if os.path.isfile(path+item):
            img = cv2.imread(path+item)
            #img = cv2.COLOR_BGR2GRAY(img)
            patches_img = patchify(img, (1000 ,1000 ,3), step=900)
            for i in range(patches_img.shape[0]):
                for j in range(patches_img.shape[1]):
                    single_patch_img = patches_img[i,j,0,:,:,:]
                    if not cv2.imwrite('C:/Users/patches/' + item + '_' + str(i) + str(j) + '.png',single_patch_img):
                        raise Exception("failed!")

makepatches()
