from pynput.mouse import Button, Controller
import serial

state = 0
running = True

#print welcome
print('----- Welcome to Mousing -----')
print('-- 1 Listening ---------------')
print('-- 2 Controlling -------------')
print('-- 3 Debugging ---------------')

# modes - 	1: listening
#			2: controlling
# 			3: debugging

#input starting mode
my_input = input('Enter desired mode: ')
mouse = Controller()

while running:
	#pass
	# check state

	# listening
	if (state == 1):
		on_click(0, 0)

	# controlling
	if (state == 2):

		# Read pointer position 
		print('The current pointer position is {0}'.format(mouse.position))

		# Set pointer position
		mouse.position = (10, 20)
		print('Now we have moved it to {0}'.format(mouse.position))

		# Move pointer relative to current position
		mouse.move(5, -5)

		# Press and release
		mouse.press(Button.left)
		mouse.release(Button.left)

		# Double click
		mouse.click(Button.left, 2)

		# Scroll two steps down
		mouse.scroll(0,2)
	
	# debugging
	if (state == 3):
		pass




def on_move(x, y):
    print('Pointer moved to {0}'.format(
        (x, y)))

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()