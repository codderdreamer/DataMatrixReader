import cv2

class Camera:
    def __init__(self):
        self.cam = None

    def connect_colourful_camera(self):
        print("Renkli kameraya bağlanılıyor...")
        self.cam = cv2.VideoCapture('/dev/v4l/by-id/usb-Arducam_Technology_Co.__Ltd._Arducam_16MP_SN0001-video-index0')
        self.cam.set(cv2.CAP_PROP_EXPOSURE, 500)
        self.cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH,400)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT,300)