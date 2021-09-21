import sys
import h5py 
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from scipy import misc
from skimage import exposure
import time
import math
import os.path
import cv2 as cv
######### for masking based on Hao's code#############
from skimage.feature import match_template
from skimage import filters
from skimage import io
from skimage.transform import downscale_local_mean as bb
#######################################################

import matplotlib.pyplot as plt
os.chdir("C:/Users/JaianthV/Desktop/")
filename_nxs = "20201205_094_Run01.cxi" 

hdf = h5py.File(filename_nxs,'r')
Image_diff_pattern =hdf.get('/entry_1/data_1/')




#data_Image_diff_pattern = np.array(Image_diff_pattern.get('SI107_20191201_image'),dtype=np.uint32)
data_Image = np.array(Image_diff_pattern.get('data'))
print ((data_Image))
stxm = Image.fromarray(np.angle(data_Image[0]))

#x=np.angle(data_Image[0])
x = np.absolute(data_Image[0])
#x=np.unwrap(x)
#x=list(np.array(x,dtype=np.uint32))
#print (np.shape(x))
plt.matshow(stxm)
plt.show()
#stxm.save('Phase_94.tiff')

