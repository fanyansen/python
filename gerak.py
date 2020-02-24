import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN)
t = 0

while True:
	input_state = GPIO.input(18)
	if input_state == True:
		print 'TERDETEKSI!! Gerakan ke-', t
		t += 1
		time.sleep(1)
