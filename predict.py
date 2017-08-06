from __future__ import print_function

from keras.models import load_model
import numpy as np
import sys
import os
import cv2
import csv
from scipy.stats import norm
import face_detection as fd


def save_predict_img(img_file, save_path):
    img = cv2.imread(img_file)
    img_drawed = fd.draw_faces(img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    faces, coordinates = fd.get_face_image(img)
    for i in range(len(faces)):
        score = predict_cv_img(faces[i])
        cv2.putText(img_drawed, str(get_AQ(score[0][0])), coordinates[i], font, 0.8, (255, 0, 0), 2)
    cv2.imwrite(save_path, img_drawed)



def get_percentage(score):
    for i in range(len(list)):
        if score < float(list[i]):
            return (i + 1.0) / 500.0


def get_AQ(score):
    score = float(score)
    percentage = get_percentage(score)
    z_score = norm.ppf(percentage)
    return int(100 + (z_score * 24))


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
with open('label.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        list.append(row['Attractiveness label'])
list.sort()

if __name__ == '__main__':
    # print(get_AQ(3))
    main()
