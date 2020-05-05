# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:52:42 2020

@author: hunny
"""
#reference: https://medium.com/coinmonks/learn-how-to-train-u-net-on-your-dataset-8e3f89fbd623

#import libaries 
import os
from PIL import Image
from skimage import data, io, filters
import numpy as np
from scipy import ndimage
import matplotlib
from matplotlib import pyplot, image
from sklearn import manifold, datasets
from pathlib import Path
from PIL import ImageOps
import random
import re
import scipy.io
import glob
from matplotlib import cm

# define paths
DATA_PATH = 'C:/Users/hunny/Desktop/purpleGrad/heart_segmentation/datawithgroundtruth/'
LABEL_PATH = 'C:/Users/hunny/Desktop/purpleGrad/heart_segmentation/data_transformed/label/'
IMAGE_PATH = 'C:/Users/hunny/Desktop/purpleGrad/heart_segmentation/data_transformed/imgs/'

#os.listdir(DATA_PATH)
#mat = scipy.io.loadmat('C:/Users/hunny/Desktop/purpleGrad/heart_ultrasound/datawithgroundtruth/Frame1063.mat')
#image1 = mat["I"]
#mask1 = mat["mask"]
#plt.imshow(image1)  
#matplotlib.image.imsave('name.png', image1)
#i = 'C:/Users/hunny/Desktop/purpleGrad/heart_segmentation/datawithgroundtruth/Frame674.mat'
#os.path.splitext(os.path.basename(i))[0]
#matplotlib.image.imsave('imgs/'+frameid+".tif", image)


#loop through all the filenames
#for i in file_names:
	#load each file into varibale raw 
    #raw = scipy.io.loadmat(DATA_PATH + i)
	#extract the masks and image arrays from mat file
	#image = raw["I"]
    #mask = raw["mask"]
    #matplotlib.image.imsave(Path(i).stem + '.png', image)
    #matplotlib.image.imsave(Path(i).stem + '.png', mask)

#resizing using PIL 
#img = Image.open('C:/Users/hunny/unet_segmentation/data/augment/Frame1114.png')
#maxsize = (300,300)
#img.thumbnail(maxsize)
#img.save('samplecropped.tif')

#cropping using scikit
#img2 = io.imread('C:/Users/hunny/unet_segmentation/data/augment/Frame1114.png')
#img=img[22:278,0:256]
#io.imsave('samplecropped.tif',img)


#attempt to combine 2 functions together 
#pulls out all the filenames that end in .mat from folder
file_names = [f for f in os.listdir(DATA_PATH) if f.endswith('.mat')]

for i in file_names:
    frameid = os.path.splitext(os.path.basename(i))[0]
    #load each file into varibale raw 
    raw = scipy.io.loadmat(DATA_PATH + i)
    #extract the masks and image arrays from mat file
    image = raw["I"]
    label = raw["mask"]
    #save the images in respective folders
	#need to find a way to convert array to image
    im = np.array(image*255, dtype = np.uint8)
    maxsize = (300,300)
    im.thumbnail(maxsize)
    la.thumbnail(maxsize)
    border = (10,22,20,22)
    im = ImageOps.crop(im, border)
    la = ImageOps.crop(la, border)
    im.save(IMAGE_PATH+frameid+'.tif')
    la.save(LABEL_PATH+frameid+'.tif')
    matplotlib.image.imsave('imgs/'+frameid+'.tif', im)
    matplotlib.image.imsave('label/'+frameid+'.tif', la)
for i in os.listdir(DATA_PATH):
    file = DATA_PATH + i
    frameid = os.path.splitext(os.path.basename(file))[0]
    img = Image.open(file)
    maxsize = (300,300)
    img.thumbnail(maxsize)
    border = (10,22,20,22)
    img = ImageOps.crop(img, border)
    img.save(frameid+'.tif')


#demo i = 'Frame1114.png'


#2 functions .mat and. tif 
#pulls out all the filenames that end in .mat from folder
file_names = [f for f in os.listdir(DATA_PATH) if f.endswith('.mat')]
#change to your working directory 

for i in file_names:
    frameid = os.path.splitext(os.path.basename(i))[0]
    #load each file into varibale raw 
    raw = scipy.io.loadmat(DATA_PATH + i)
    #extract the masks and image arrays from mat file
    image = raw["I"]
    label = raw["mask"]
    #save the images in respective folders
    matplotlib.image.imsave('imgs/'+frameid+'.png', image)
    matplotlib.image.imsave('labels/'+frameid+'.png', label)


#original 
for i in os.listdir(DATA_PATH):
    file = "C:/Users/hunny/Desktop/purpleGrad/heart_segmentation/unet_segmentation_1/data/original/"+ i
    frameid = os.path.splitext(os.path.basename(file))[0]
    img = Image.open(file)
    maxsize = (300,300)
    img.thumbnail(maxsize)
    border = (10,22,20,22)
    img = ImageOps.crop(img, border)
    img.save(frameid+'.tif')
