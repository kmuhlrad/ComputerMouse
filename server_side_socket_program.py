#server side socket program
#batbot echos servo protocol
#Created by Brandon Nguyen
#Copied and commented (more) by Madison Evans

# FTP = File Transfer rotocol - standard network protocol used
#for transfer ofcomp files between client and server on a network
from ftplib import FTP
import socket
import time
import os
#import thread
#import threading

import serial
import sys

while True:
    host = '' #Symbolic name meaning all available interfaces
    port = 50420 # Arbitrar non-priveleged port
    
    #Initialize Serial
    ser = serial.Serial('/dev/ttyUSB0',9600)
    
    #Create data folder (if it doesn't exist) and navigate to its path
    data_path = '/home/pi/DATA/'
    
    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    os.chdir(data_path)
    
    ftp_logged = False
    
    while ftp_logged == False:
        try:
            #FTP
            #**** CHANGE BELOW PARAM ******                                               
            ftp = FTP('169.254.32.143') #IP address of host
            ftp.login('admin','bats123')
            
            ftp.cwd('/ni-rt/startup/') #Changes to specified ftp directory
            ftp_logged = True
            
            print("FTP connection established.")
            #****************************
            
        except:
            pass
        
        time.sleep(1)
    
    #Socket Server Setup
    s = socket.socket(socket.AF_inet6, socket.SOCK_STREAM)
    print("Socket Connected.")
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    
    print("Socket bound.")
    print("Listening for client(s)...")
    
    s.listen(1)
    conn,address = s.accept()
    print("Connected to {} @ {}".format(str(address[0]),str(address[1])))
    
    run = 0
    
    while True: 
       #Receive command from client to:
       #Tell sbRIO to do things, receive/delete datafile from it
       time_total = time.time()
       data = conn.recv(1024).decode().strip()
            
       if data == "run":
                ser.write("0") # Run sbRIO loop once
            time_ready = time.time()
            ready_signal = ser.readline().strip()
            print("Time for sbrio to finish: " + str(time.time() - time_ready))
            if ready_signal == "read": # reads "ready" from sbrio
                time retr = time.time()
                print("making file #" + str(run + 1))
                ftp.retrbinary("RETR sbrio_data", open('datafile.dat','wb').write) #Retrive specified file from ssbrIO
                print("deleting file")
                ftp.delete('sbrio_data') #deletes specified file from sbRIO
                print("Done: " + str(time.tim() - time_retr))
                with open(data_path + 'datafile.dat', 'rb') as fid:
                    for line in fid:
                        conn.send(line)
                    time.sleep(0.2)
                    conn.send(b'done')
                run = run + 1
                print (run)
                print("Time to transfer file: " + str(time.time() - time.filewrite))
        elif data == "quit":
            break
            
        print("Total loop time:" + str(time.time() - time_total))
        time.sleep(0.05)
    ftp.quit()
    conn.close()
    time.sleep(1)
    
    