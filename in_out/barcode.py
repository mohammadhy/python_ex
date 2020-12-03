import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
from datetime import datetime
import sqlite3
import logging
#======================(define Log)========================================
logger = logging.getLogger(__name__)
stream_log = logging.StreamHandler()
save_log = logging.FileHandler('barcode.log')

logger.setLevel(logging.INFO)
stream_log.setLevel(logging.WARNING)
save_log.setLevel(logging.INFO)

stream_log_format =logging.Formatter('%(name)s - %(levelname)s - %(message)s') 
save_log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_log.setFormatter(stream_log_format)
save_log.setFormatter(save_log_format)

logger.addHandler(stream_log)
logger.addHandler(save_log)

#======================(define sqlite)========================================
with sqlite3.connect('in_out.db') as db :
    c = db.cursor()
    
c.execute('''
CREATE TABLE IF NOT EXISTS person (
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
incomDate timestamp,
outDate timestamp);
''')
db.commit()




#=============================================================================
cap = cv2.VideoCapture(0)
out_info = set()
lst_out_info = list(out_info)

f_info = set()
present_info = []


now = datetime.now()
#=============================================================================
def incom():

    while True:
        _, frame = cap.read()

        decod = pyzbar.decode(frame)
        for obj in decod:
            t = str(obj.data)
            z = t.split("'")
            n = z[1].split("_")
            print(f'You {n[1]} Present  By Id {n[0]} ')
            present_info.append(n[1])
            present_info.append(n[0])
            present_info.append(str(now))
            lst = [present_info[0], present_info[1], present_info[2]]
            f_info.update(lst)
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
    try:
        with sqlite3.connect('in_out.db') as db :
                cursor = db.cursor()
                insert = 'INSERT INTO person(userID ,username, incomDate) VALUES (?,?,?)'
                cursor.execute(insert,[(present_info[1]),(present_info[0]), (present_info[2]) ])
                db.commit()
                logger.info(f'This Person {present_info[0]} By Id {present_info[1]} Come At {present_info[2]}')
    except:
        logger.exception('This Error Occure:')
#=============================================================================
def out():

    while True:
        _, frame = cap.read()

        decod = pyzbar.decode(frame)
        for obj in decod:
            t = str(obj.data)
            z = t.split("'")
            n = z[1].split("_")
            print(f'You {n[1]} Present  By Id {n[0]} ')
            out_info.update([n[1], n[0], str(now)])
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
    try:
        with sqlite3.connect('in_out.db') as db :
            cursor = db.cursor()
            #find = ('SELECT expiretime FROM new_developers WHERE name = ? and password = ?')
            #insert = 'INSERT INTO person(userID ,username, outDate) VALUES (?,?,?)'
            update = ('UPDATE person SET outDate = ? WHERE username =?')
            cursor.execute(update,[(lst_out_info[2]), (lst_out_info[1])])
            db.commit()
            logger.info(f'This Person {lst_out_info[1]}  Out At {lst_out_info[2]}')
    except:       
            logger.exception('This Error Occure:')
#=============================================================================

income = input('incoming or out :')
if income == 'out':
    out()
elif income == 'incoming':
    incom()
#=============================================================================









