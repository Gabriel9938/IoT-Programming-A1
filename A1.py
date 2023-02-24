import serial
import MySQLdb
import datetime
import time
from flask import Flask, render_template

device = '/dev/ttyACM0'

arduino = serial.Serial(device,115200)

while 1:
    dbConn = MySQLdb.connect("localhost","pi","","PlantCare_db") or die("Could not connect to the database")
    
    while(arduino.in_waiting == 0):
        pass
    line = arduino.readline()
    Humidity = str(line[19:25])
    HumidityInt = float(line[19:21])
    Temp = str(line[41:47])
    TempInt = float(line[41:43])
    Movement = str(line[60:61])
    Today = datetime.datetime.now()
    Date = str(Today.strftime("%x"))
    Time = str(Today.strftime("%X"))
    
    command = "";
    
    print(arduino.readline().decode('ascii'))
    
    if(HumidityInt < 60):
        command += "on"
        #arduino.write("on".encode())
        Watering = "Yes"
    elif(HumidityInt >= 60):
        command += "off"
        #arduino.write("off".encode())
        Watering = "No"
            
    if(Movement == "b'Y'"):
        command +="play"
        #arduino.write("play".encode())
        Movement2 = "Yes"
    else:
        command += ""
        Movement2 = "No"
        
    if(command !="" ):
        arduino.write(command.encode())
        #print(command)
        

    
    #print (Movement)
    time.sleep(0.2)
    
    
    
    with dbConn:
        cursor = dbConn.cursor()
        sql = "INSERT INTO activityLog (Date, Time, Humility, Temperature, Shocked, Watering) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (Date, Time, str(HumidityInt) + "%", str(TempInt) + "C", Movement2, Watering)
        cursor.execute(sql,value)
        dbConn.commit() 
        cursor.close()

