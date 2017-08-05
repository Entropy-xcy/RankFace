from keras.models import load_model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import sys
import os
import cv2
import csv


def get_AQ(score):
    score = float(score)
    i = 0
    for i in range(len(list)):
        i += 1
        if score < float(list[i]):
            break
    percentage = i / 500



def load_image(file):
    image = cv2.imread(file)
    image = cv2.resize(image, (128, 128))
    image = image / 255
    image = np.expand_dims(image, axis=0)
    return image


def predict_cv_img(img):
    img = cv2.resize(img, (128, 128))
    img = img / 255
    img = np.expand_dims(img, axis=0)
    return predict(img)


def predict(img):
    return model.predict(img) * 5.0


def training_test():
    filelist = os.listdir('./data')
    for i in filelist:
        print(i, '  ', predict(load_image('./data/' + i)))


def main():
    for i in sys.argv:
        if i.find('.jpg') != -1:
            print(predict(load_image(i)))


model = load_model('faceRank.h5')
list = []
with open('./label.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list.append(row['Attractiveness label'])
list.sort()

if __name__ == '__main__':
    # print(get_AQ(3))
    main()
