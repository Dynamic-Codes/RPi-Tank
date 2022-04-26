'''
#CODE MADE BY DYNAMIC_CODES
#DO NOT USE WITHOUT PERMISSION
#COPYRIGHT 2022
#ALL RIGHTS RESERVERD
'''

print('''
#CODE MADE BY DYNAMIC_CODES
#DO NOT USE WITHOUT PERMISSION
#COPYRIGHT 2022
#ALL RIGHTS RESERVERD
''')

import time
from pynput.keyboard import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

motor1a = 7
motor1b = 11
motor1e = 22

motor2a = 13
motor2b = 16
motor2e = 15

wKey = False
aKey = False
sKey = False
dKey = False

def MTRC_out():
	GPIO.setup(motor1a,GPIO.OUT)
	GPIO.setup(motor1b,GPIO.OUT)
	GPIO.setup(motor1e,GPIO.OUT)
	GPIO.setup(motor2a,GPIO.OUT)
	GPIO.setup(motor2b,GPIO.OUT)
	GPIO.setup(motor2e,GPIO.OUT)

def MTRC_idle():
	GPIO.output(motor1a,GPIO.LOW)
    	GPIO.output(motor1b,GPIO.LOW)
    	GPIO.output(motor1e,GPIO.LOW)
    	GPIO.output(motor2a,GPIO.LOW)
	GPIO.output(motor2b,GPIO.LOW)
	GPIO.output(motor2e,GPIO.LOW)

MTRC_out()

def KeyArmed(key_type):
	global wKey
	global aKey
	global sKey
	global dKey
	
	if (key_type == KeyCode.from_char('w')) or (key_type == Key.up):
		if wKey == False:
			wKey = True
			print('[MTRC] Activating forward roll.')
			GPIO.output(motor1a,GPIO.HIGH)
            		GPIO.output(motor1b,GPIO.LOW)
            		GPIO.output(motor1e,GPIO.HIGH)
            		GPIO.output(motor2a,GPIO.LOW)
            		GPIO.output(motor2b,GPIO.HIGH)
  			GPIO.output(motor2e,GPIO.HIGH)

		#
	if (key_type == KeyCode.from_char('a')) or (key_type == Key.left):
		if aKey == False:
			aKey = True
			print('[MTRC] Activating left roll.')
			GPIO.output(motor1a,GPIO.HIGH)
            		GPIO.output(motor1b,GPIO.LOW)
            		GPIO.output(motor1e,GPIO.HIGH)
            		GPIO.output(motor2a,GPIO.HIGH)
			GPIO.output(motor2b,GPIO.LOW)
			GPIO.output(motor2e,GPIO.HIGH)

		#
	if (key_type == KeyCode.from_char('s')) or (key_type == Key.down):
		if sKey == False:
			sKey = True
			print('[MTRC] Activating reverse roll.')
			GPIO.output(motor1a,GPIO.LOW)
            		GPIO.output(motor1b,GPIO.HIGH)
            		GPIO.output(motor1e,GPIO.HIGH)
            		GPIO.output(motor2a,GPIO.HIGH)
			GPIO.output(motor2b,GPIO.LOW)
			GPIO.output(motor2e,GPIO.HIGH)

		#
	if (key_type == KeyCode.from_char('d')) or (key_type == Key.right):
		if dKey == False:
			dKey = True
			print('[MTRC] Activating right roll.')
			GPIO.output(motor1a,GPIO.LOW)
            		GPIO.output(motor1b,GPIO.HIGH)
            		GPIO.output(motor1e,GPIO.HIGH)
            		GPIO.output(motor2a,GPIO.LOW)
			GPIO.output(motor2b,GPIO.HIGH)
			GPIO.output(motor2e,GPIO.HIGH)

		#
		

def KeyDisarmed(key_type):
	global wKey
	global aKey
	global sKey
	global dKey

	if (key_type == KeyCode.from_char('w')) or (key_type == Key.up):
		print('[MTRC] Set motor status to idle.')
		wKey = False
		MTRC_idle()

	if (key_type == KeyCode.from_char('a')) or (key_type == Key.left):
		print('[MTRC] Set motor status to idle.')
		aKey = False
		MTRC_idle()

	if (key_type == KeyCode.from_char('s')) or (key_type == Key.down):
		print('[MTRC] Set motor status to idle.')
		sKey = False
		MTRC_idle()

	if (key_type == KeyCode.from_char('d')) or (key_type == Key.right):
		print('[MTRC] Set motor status to idle.')
		dKey = False
		MTRC_idle()

	#Tank Off.
	if key_type == Key.esc:
		print('[MTRC] Shutting down motors...')
		MTRC_out()
		print('[MTRC] All motors out.')
		time.sleep(1)
		print('[PRGM] Exiting in 5 seconds.')
		time.sleep(5)
		exit()
		quite()

with Listener(on_press = KeyArmed, on_release = KeyDisarmed) as listener:
	listener.join()

'''
#CODE MADE BY DYNAMIC_CODES
#DO NOT USE WITHOUT PERMISSION
#COPYRIGHT 2022
#ALL RIGHTS RESERVERD
'''
