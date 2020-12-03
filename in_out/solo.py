import datetime
import pyqrcode
import png
import pyzbar.pyzbar as pz
import cv2


name = 'ahmad'
x = '123947'
print(f'{name.title()}  By Id {x} Present At Work')
qr = pyqrcode.create(x +'_'+ name)
qr.png('qr2.png', scale = 5)
print(qr)

img = cv2.imread('qr2.png')
decod = pz.decode(img)
for obj in decod:
    t = str(obj.data)
    z = t.split("'")
    n = z[1].split("_")
    
print(f'You {n[1].title()} Present By Id {n[0]} At Work')










