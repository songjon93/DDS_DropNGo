import DB
import watson_helper
import rfid_module
import output_module
from time import sleep

while True:
    led_module.led_on()
    uid = rfid_module.scan()
    led_module.led_off()

    print("Inspecting To Go Box.\n")
    classifier_res = watson_helper.ask_watson_list("./images/f_test_1.JPG")

    if (classifier_res[0][1] < 0):
        print("This is not a certified To Go Box.\n")
        continue

    # DB.update(DB.col, uid, 1)
    if (DB.query(DB.col, uid) < 0):
        DB.new(DB.col, uid)

    print("You have {} boxes remaining.\n".format(DB.update(DB.col, uid, 1)))

    sleep(5)
