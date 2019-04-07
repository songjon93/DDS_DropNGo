import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

ledPin = 27
push_button = 22
buzzer = 23

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(push_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
def led_on():
	GPIO.output(ledPin, GPIO.HIGH)

def led_off():
	GPIO.output(ledPin, GPIO.LOW)

def clean_up():
	GPIO.clean_up()
