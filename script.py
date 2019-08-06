import numpy
import sys
import time
from PIL import *
def open_image(path):
    image =[]
    try:
        image=Image.open(path)
    except Exception as e:
         print(e)
    return image
debut = time.time()
image = open_image("/media/yohan/NIKON D80/DCIM/100NCD80/DSC_5202.NEF")
image.show()
fin = time.time()
moyenne = fin-debut
print("{}s".format(moyenne))
