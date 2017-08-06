import cv2
import sys
import predict
import face_detection as fd


if __name__ == '__main__':
    for i in sys.argv:
        if i.find('.jpg') != -1:
            img = cv2.imread(i)
            img_drawed = fd.draw_faces(img)
            font = cv2.FONT_HERSHEY_SIMPLEX
            faces, coordinates = fd.get_face_image(img)
            for i in range(len(faces)):
                score = predict.predict_cv_img(faces[i])
                cv2.putText(img_drawed, str(predict.get_AQ(score[0][0])), coordinates[i], font, 0.8, (255, 0, 0), 2)
            fd.show(img_drawed)
