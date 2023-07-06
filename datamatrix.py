import cv2
from pylibdmtx import pylibdmtx
import threading

readed = True

def decode_frame(frame):
    global readed
    readed = False
    print("decode ediliyor")
    data = pylibdmtx.decode(frame)
    print(data)
    readed = True


vid = cv2.VideoCapture('/dev/v4l/by-id/usb-Arducam_Technology_Co.__Ltd._Arducam_16MP_SN0001-video-index0')
vid.set(cv2.CAP_PROP_EXPOSURE, 500)
vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
vid.set(cv2.CAP_PROP_FRAME_WIDTH,400)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,300)

while(True):
    try:
        # Capture the video frame
        # by frame
        # print("frame alınıyor.")
        ret, frame = vid.read()
    
        # Display the resulting frame
        if ret:
            cv2.imshow('frame', frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            ret,thresh = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # print("decode baş.")

            if readed == True:
                threading.Thread(target=decode_frame,args=(thresh,),daemon=True).start()
            
        else:
            print("frame yok")
      
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    except Exception as e:
        print("except",e)
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

