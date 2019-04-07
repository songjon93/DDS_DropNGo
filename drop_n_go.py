import subprocess
import DB
import watson_helper
import rfid_module
import output_module
from time import sleep

img = "i.jpg"

while True:
    output_module.led_on()
    uid = rfid_module.scan()
    output_module.led_off()

    print("Inspecting To Go Box.\n")
    subprocess.run(["sudo", "fswebcam", img])
    classifier_res = watson_helper.ask_watson_list(img)
    print(classifier_res)
    if (classifier_res[0][1] < 0):
        print("This is not a certified To Go Box.\n")
        output_module.buzzer_wrong()
        continue

    # output_module.buzzer_on();
    output_module.buzzer_correct()

    # motor move
    output_module.set_angle(90)
    # DB.update(DB.col, uid, 1)
    if (DB.query(DB.col, uid) < 0):
        DB.new(DB.col, uid)
    sleep(3)
    output_module.set_angle(180)
    # playSong(starwars_notes, starwars_beats, 0.2)
    sleep(.5)
    print("You have {} boxes remaining.\n".format(DB.update(DB.col, uid, 1)))
    # output_module.buzzer_off();
    sleep(3)
