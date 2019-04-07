import DB
import watson_helper
import rfid_module
import output_module
from time import sleep

while True:
    output_module.led_on()
    uid = rfid_module.scan()
    output_module.led_off()

    print("Inspecting To Go Box.\n")
    classifier_res = watson_helper.ask_watson_list("./images/f_test1.JPG")

    print(classifier_res)
    if (classifier_res[0][1] < 0):
        print("This is not a certified To Go Box.\n")
        continue

    # DB.update(DB.col, uid, 1)
    if (DB.query(DB.col, uid) < 0):
        DB.new(DB.col, uid)

    output_module.buzzer_on();
    sleep(0.5)
    print("You have {} boxes remaining.\n".format(DB.update(DB.col, uid, 1)))
    output_module.buzzer_off();
