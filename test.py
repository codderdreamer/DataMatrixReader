import cv2
# from pylibdmtx import pylibdmtx
import threading
import numpy as np
from ModbusModule import *

#import zxingcpp
#import numpy

from dbr import BarcodeReader, EnumErrorCode

readed = True

modbus = ModbusModule()

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
vid.set(cv2.CAP_PROP_FRAME_WIDTH,1600)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT,1200)

modbus.connect_modbus()
time.sleep(5)
modbus.open_white_led()

while(True):
    try:
        # Capture the video frame
        # by frame
        # print("frame alınıyor.")
        ret, frame = vid.read()


        # Display the resulting frame
        if ret:
            matrix = cv2.getPerspectiveTransform(np.float32([[563,208],[562,1099],[1389,215],[1380,1092]]),np.float32([[0,0],[0,700],[700,0],[700,700]]))
            frame = cv2.warpPerspective(frame,matrix,(700,700))

            cv2.imshow('frame', frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            ret,thresh = cv2.threshold(frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            # print("decode baş.")

            # if readed == True:
            #     threading.Thread(target=decode_frame,args=(thresh,),daemon=True).start()
            
            #1
            #np_arr = numpy.array(frame)
            #results = zxingcpp.read_barcodes(np_arr)
            #print(results)

            #2 Çok hızlı ama ücretli
            reader = BarcodeReader()
            results = reader.decode_buffer(frame)
            if results != None:
               for text_result in results:
                   print("Barcode Format : ")
                   print(text_result.barcode_format_string)
                   print("Barcode Text : ")
                   print(text_result.barcode_text)
                   print("Localization Points : ")
                   print(text_result.localization_result.localization_points)
                   print("Exception : ")
                   print(text_result.exception)
                   print("-------------")
                   print(results)
            
        else:
            print("frame yok")
      
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            modbus.close_all_coils()
            break

    except Exception as e:
        print("except",e)
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
