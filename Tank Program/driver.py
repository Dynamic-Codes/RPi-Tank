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

wKey = False
aKey = False
sKey = False
dKey = False


def KeyArmed(key_type):
	#print('Key Active: {}'.format(key_type))
	global wKey
	global aKey
	global sKey
	global dKey
	
	if (key_type == KeyCode.from_char('w')) or (key_type == Key.up):
		if wKey == False:
			wKey = True
			print('[MTRC] Activating forward roll.')

		#
	if (key_type == KeyCode.from_char('a')) or (key_type == Key.left):
		if aKey == False:
			aKey = True
			print('[MTRC] Activating left roll.')

		#
	if (key_type == KeyCode.from_char('s')) or (key_type == Key.down):
		if sKey == False:
			sKey = True
			print('[MTRC] Activating reverse roll.')

		#
	if (key_type == KeyCode.from_char('d')) or (key_type == Key.right):
		if dKey == False:
			dKey = True
			print('[MTRC] Activating right roll.')

		#
		

def KeyDisarmed(key_type):
	#print('Key Disabled: {}'.format(key_type))
	global wKey
	global aKey
	global sKey
	global dKey

	if (key_type == KeyCode.from_char('w')) or (key_type == Key.up):
		print('[MTRC] Set motor status to idle.')
		wKey = False

	if (key_type == KeyCode.from_char('a')) or (key_type == Key.left):
		print('[MTRC] Set motor status to idle.')
		aKey = False

	if (key_type == KeyCode.from_char('s')) or (key_type == Key.down):
		print('[MTRC] Set motor status to idle.')
		sKey = False

	if (key_type == KeyCode.from_char('d')) or (key_type == Key.right):
		print('[MTRC] Set motor status to idle.')
		dKey = False


	

	#Tank Off.
	if key_type == Key.esc:
		print('[MTRC] Shutting down motors...')
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