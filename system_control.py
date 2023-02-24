# led_control.py
import serial
import time
import MySQLdb
import datetime
from flask import Flask, render_template
app = Flask (__name__)
# Dictionary of pins with name of pin and state ON/OFF

# Main function when accessing the website
@app.route("/")
def index():
 # TODO: Read the status of the pins ON/OFF and update dictionary
 # This data will be sent to index.html (pin dictionary)
 templateData = {
     'pins1' : data1
 }
 # Pass the template data into the template index.html and return it
 return render_template('index.php', **templateData)
# Function to send simple commands
@app.route("/<action>")
def action(action):
 data1=list()
 if action == 'action1' :
     ser.write("1")
 if action == 'action2' :
     ser.write("2")
 if action == 'action3' :
     ser.write("3")
 if action == 'action4' :
    command = ""
    line = arduino.readline()
    Humidity = str(line[19:25])
    HumidityInt = float(line[19:21])
    Temp = str(line[41:47])
    TempInt = float(line[41:43])
    Movement = str(line[60:61])
    Today = datetime.datetime.now()
    Date = str(Today.strftime("%x"))
    Time = str(Today.strftime("%X"))
    
    if(HumidityInt > 60):
        command += "on"
        #arduino.write("on".encode())
        Watering = "Yes"
    elif(HumidityInt <= 60):
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
        ser.write(command.encode())
        #print(command)
    
    with dbConn:
        cursor = dbConn.cursor()
        sql = "INSERT INTO activityLog (Date, Time, Humility, Temperature, Shocked, Watering) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (Date, Time, str(HumidityInt) + "%", str(TempInt) + "C", Movement2, Watering)
        cursor.execute(sql,value)
        cursor.execute("SELECT * FROM activityLog")
        dataList = cursor.fetchall()
        for x in dataList:
            data1.append(x)
        cursor.close()
 with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("SELECT * FROM activityLog")
        dataList = cursor.fetchall()
        for x in dataList:
            data1.append(x)
        cursor.close()
 # This data will be sent to index.html (pins dictionary)
 templateData = {
     'pins1' : data1
 }
 # Pass the template data into the template index.html and return it
 return render_template('index.php', **templateData)

# Main function, set up serial bus, indicate port for the webserver, and start the service
if __name__ == "__main__" :
    data1 = list();
    device = '/dev/ttyACM0'
    ser = serial.Serial(device, 115200, timeout = 1)
    arduino = serial.Serial(device,115200)
    
    dbConn = MySQLdb.connect("localhost","pi","","PlantCare_db") or die("Could not connect to the database")
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("SELECT * FROM activityLog")
        dataList = cursor.fetchall()
        for x in dataList:
            data1.append(x)
        cursor.close()
    ser.flush()
    app.run(host='0.0.0.0', port = 80, debug = True)