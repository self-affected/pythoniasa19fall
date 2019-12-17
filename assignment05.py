import cv2
import logging
from pathlib import Path
import time

CASCADESFILE = 'data/haarcascades/haarcascade_frontalface_default.xml'
EYESFILE = 'data/haarcascades/haarcascade_eye.xml'
SMILEFILE = 'data/haarcascades/haarcascade_smile.xml'
LOGFILE = 'build/faces.log'

Path('build').mkdir(exist_ok=True)
logging.basicConfig(filename=LOGFILE, level='DEBUG')

def main():
# all( (x1 <= x <= x + w <= x1 + w ) and (y1 <= y <= y + h <= y1 + h) for (x1,y1,h1,w1) in faces)
    model = cv2.CascadeClassifier(CASCADESFILE)
    modeleyes = cv2.CascadeClassifier(EYESFILE)
    modelsmile = cv2.CascadeClassifier(SMILEFILE)

    webcam = cv2.VideoCapture(0)

    # infinite image processing loop
    while True:

        if not webcam.isOpened():
            logging.warning('Unable to connect to camera.')
            time.sleep(5)
            continue

        # get image from camera
        ret, frame = webcam.read()

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # convert image to grayscale
        grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        grayframe = cv2.GaussianBlur(grayframe, (21, 21), 0)

        adap_gaussian_8 = cv2.adaptiveThreshold(grayframe, 255,
                                                cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                                cv2.THRESH_BINARY, 199, 5)




        # detect faces scaleFactor=3.1, minNeighbors=5, minSize=(30, 30)
        faces = model.detectMultiScale(adap_gaussian_8, scaleFactor=3.1, minNeighbors=5, minSize=(30, 30))
        eyes = modeleyes.detectMultiScale(grayframe, scaleFactor=3.1, minNeighbors=5, minSize=(40, 40))
        smile = modelsmile.detectMultiScale(grayframe, scaleFactor=3.1, minNeighbors=5, minSize=(40,40))
        logging.info(f'Detected faces: {len(faces)}')

        # add boxes
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        for (x, y, w, h) in eyes:
            if bool(list(faces)):
                if all( (x1 <= x <= x + w <= x1 + w1 ) and (y1 <= y <= y + h <= y1 + h1) for (x1,y1,h1,w1) in faces):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (x, y, w, h) in smile:
            if bool(list(faces)):
                if all( (x1 <= x <= x + w <= x1 + w1 ) and (y1 <= y <= y + h <= y1 + h1) for (x1,y1,h1,w1) in faces):
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


        # show image
        cv2.imshow('Video', frame)

        # stop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # close everything
    webcam.release()
    cv2.destroyWindows()


if __name__ == '__main__':
    main()
