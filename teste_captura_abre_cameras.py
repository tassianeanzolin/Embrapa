import cv2
import threading


class CamThread(threading.Thread):
    def __init__(self, PreviewName, CamId):
        threading.Thread.__init__(self)
        self.PreviewName = PreviewName
        self.CamId = CamId

    def run(self):
        print('Starting' + self.PreviewName)
        CamPreview(self.PreviewName, self.CamId)



def CamPreview(PreviewName, CamId, x=0):
    cv2.namedWindow(PreviewName)
    cam = cv2.VideoCapture(CamId)
    if cam.isOpened():
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        rval, frame = cam.read()
        cv2.imshow(PreviewName, frame)

        cv2.imwrite('captura/' + str(PreviewName) + ' Frame' + str(x) + '.jpg', frame)
        x += 1

        key = cv2.waitKey(1000)
        if key == 27:  # saída com ESC
            break
    cv2.destroyWindow(PreviewName)


# Cria as threads

thread1 = CamThread("Camera 1", 1)
thread2 = CamThread("Camera 2", 2)
thread3 = CamThread("Camera 3", 3)
thread4 = CamThread("Camera 4", 4)
thread1.start()
thread2.start()
thread3.start()
thread4.start()
