import os
import tensorflow as tf
import numpy as np
import cv2 as cv

def create_training_set():
    path = 'Faces/'
    training_set = []

    for img in os.listdir(path):
        try:
            img_arr = cv.imread(os.path.join(path,img),0)
            img_resize = cv.resize(img_arr,(50,50))
            training_set.append(img_resize)
        except:
            pass







