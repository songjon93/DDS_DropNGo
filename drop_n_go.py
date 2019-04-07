import DB
import watson_helper
import rfid_module
from time import sleep

while True:
    uid = rfid_module.scan()
    # DB.update(DB.col, uid, 1)
    if (DB.query(DB.col, uid) < 0):
        DB.new(DB.col, uid)

    print("You have {} boxes remaining".format(DB.update(DB.col, uid, 1)))

    sleep(5)
