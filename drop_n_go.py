import DB
import watson_helper
import rfid_module

rfid_module.init()
while True:
    rfid_module.scan()
