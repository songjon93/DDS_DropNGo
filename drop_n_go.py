import DB
import watson_helper
import rfid_module
import led_module
from time import sleep

while True:
    led_module.led_on()
    uid = rfid_module.scan()
    led_module.led_off()
    
    # DB.update(DB.col, uid, 1)
    if (DB.query(DB.col, uid) < 0):
        DB.new(DB.col, uid)

    print("You have {} boxes remaining".format(DB.update(DB.col, uid, 1)))

    sleep(5)
