import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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

CORRECT =	[["c6",4], ["a5", 4]]
WRONG = [["ab4", 2]]

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


GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(push_button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback)
def led_on():
	GPIO.output(ledPin, GPIO.HIGH)

def led_off():
	GPIO.output(ledPin, GPIO.LOW)

def buzzer_on():
    GPIO.output(buzzer, 1)

def buzzer_off():
    GPIO.output(buzzer, 0)

def playScale(scale, pause):
    '''
    scale: scale name to be played
    pause: pause between each notes played

    This function plays the given scale in every available octave
    I used this to test what was audible on the buzzer
    '''
    for i in range(0, 5):
        for note in scale:
            tone1.ChangeFrequency(note[i])
            time.sleep(pause)
    tone1.stop()

def playSong(songnotes, songbeats, tempo):
    '''
    songnotes: list of the melodies notes
    songbeats: list of melodies beat times
    tempo: speed of song, this is not traditional tempo in bpm like on a metronome,
        but more like a multiplier for whatever the notes are so a tempo value of 2
        make it play twice as fast. Adjust this by ear.

    This function plays the melody, simply by iterating through the list.
    '''
    tone1.ChangeDutyCycle(50)
    for i in range(0, len(songnotes)):
        tone1.ChangeFrequency(songnotes[i])
        time.sleep(songbeats[i]*tempo)
    tone1.ChangeDutyCycle(0)

def clean_up():
	GPIO.clean_up()
