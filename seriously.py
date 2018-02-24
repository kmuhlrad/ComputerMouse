import serial, time
port = 'COM3'
comm = serial.Serial(port, 115300, timeout = 5)


while True:
	serialData = comm.readLine()
	splitData = serialData.split(',')
	try:
		left_click 		= bool(splitData[0])
        right_click 	= bool(splitData[1])
        enabled 		= bool(splitData[2])
        delta_accel_x 	= float(splitData[3])
        delta_accel_y 	= float(splitData[4])
    except:
    	print('Cannot parse')
    print('left click:', left_click, 'rightclick:', right_click, 'velocity y:', delta_accel_y, 'velocity x:', delta_accel_x)

    time.sleep(2)

