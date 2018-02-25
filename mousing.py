from pynput.mouse import Button, Controller

mouse = Controller()

while mouse_enabled:

	if left_click:
		mouse.click(Button.left)
		continue
	elif right_click:
		mouse.click(Button.right)
		continue

	# Move pointer relative to current position
	mouse.move()

'''
# Read pointer position
print('The current pointer position is', mouse.position)

# Set pointer position
mouse.position = (10, 20)
mouse.position
print('Now we have moved it to', mouse.position)

# Move pointer relative to current position
mouse.move(5, -5)
'''