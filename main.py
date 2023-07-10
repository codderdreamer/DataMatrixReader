import cv2
from pylibdmtx import pylibdmtx           # test edildi ücretsiz ama bazen okumuyor. sorunlu çalışıyor.
import threading
import numpy as np
from ModbusModule import *

#import zxingcpp                                            # boş dönüyor çalışmıyor
#import numpy

# from dbr import BarcodeReader, EnumErrorCode              # ücretli çok iyi çalışıyor


modbus = ModbusModule()
modbus.connect_modbus()
time.sleep(5)
modbus.open_white_led()

print("Barkod Okuma Başlatıldı...")



