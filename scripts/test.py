import sys, getopt, bluetooth

sys.path.append('.')
import RTIMU
import os.path
import time
import math

SETTINGS_FILE = "RTIMULib"

# Grabs sensor
s = RTIMU.Settings(SETTINGS_FILE)
imu = RTIMU.RTIMU(s)

# Exits if cannot initilize the sensor
if (not imu.IMUInit()):
    sys.exit(1)

# this is a good time to set any fusion parameters
imu.setSlerpPower(0.02)
imu.setGyroEnable(True)
imu.setAccelEnable(True)
imu.setCompassEnable(True)

poll_interval = imu.IMUGetPollInterval()

server_sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

port = 1
server_sock.bind(("",port))
server_sock.listen(1)

client_sock,address = server_sock.accept()

while True:
  
    if imu.IMURead():
        print "Alive"
    
        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
       
        s = ("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]), math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))

        print "About to print s"
        print s
        client_sock.send(s)
    
        #time.sleep(poll_interval*1.0/1000.0)

print "All done"
client_sock.close()
server_sock.close()
