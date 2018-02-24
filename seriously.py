import serial
port = 'COM3'

while True:
	serialData = self.comm.readLine()
	splitData = serialData.split(',')
	try:
		left_click 		= bool(splitData[0])
        right_click 	= bool(splitData[1])
        enabled 		= bool(splitData[2])
        delta_accel_x 	= float(splitData[3])
        delta_accel_y 	= float(splitData[4])
    except:
    	print('Cannot parse')

