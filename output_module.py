import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

servo = 4
ledPin = 27
push_button = 22
buzzer = 18

SPEED = 1

# List of tone-names with frequency
TONES = {"c6":1047,
	"b5":988,
	"a5":880,
	"g5":784,
	"f5":698,
	"e5":659,
	"eb5":622,
	"d5":587,
	"c5":523,
	"b4":494,
	"a4":440,
	"ab4":415,
	"g4":392,
	"f4":349,
	"e4":330,
	"d4":294,
	"c4":262}

CORRECT = [["a5", 32], ["c5", 16]]
WRONG = [["ab4", 3]]

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(push_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(servo, GPIO.OUT)
motor = GPIO.PWM(servo, 50)

# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
def led_on():
	GPIO.output(ledPin, GPIO.HIGH)

def led_off():
	GPIO.output(ledPin, GPIO.LOW)

def buzzer_on():
    GPIO.output(buzzer, 1)

def buzzer_off():
    GPIO.output(buzzer, 0)

def buzzer_correct():
	p = GPIO.PWM(buzzer, 440)
	p.start(0.5)
	for t in CORRECT:
		playTone(p, t)

def buzzer_wrong():
	p = GPIO.PWM(buzzer, 440)
	p.start(0.5)
	for t in WRONG:
		playTone(p, t)

# def set_angle(fr, to, vec):
# 	for i in range(fr, to, vec):
# 	    duty = 1./18. * i + 2
# 	    # GPIO.output(servo, True)
# 	    motor.ChangeDutyCycle(duty)
# 	    time.sleep(0.02)
# 	    # GPIO.output(servo, True)
# 	    # motor.ChangeDutyCycle(0)

def set_angle(angle):
	duty = 1.0/18.0 * angle + 2
	motor.ChangeDutyCycle(duty)
	time.sleep(1)
	motor.ChangeDutyCycle(0)

def playTone(p, tone):
        # calculate duration based on speed and tone-length
	duration = (1./(tone[1]*0.25*SPEED))

	if tone[0] == "p": # p => pause
			time.sleep(duration)
	else: # let's rock
		frequency = TONES[tone[0]]
		p.ChangeFrequency(frequency)
		p.start(0.5)
		time.sleep(duration)
		p.stop()

def clean_up():
	GPIO.clean_up()

motor.start(0)
# set_angle(0, 180, 1)
# set_angle(180, 0, -1)
# motor.ChangeDutyCycle(12)
# time.sleep(1);
set_angle(90)
sleep(3)
set_angle(180)
# # set_angle(0)
# motor.stop()
