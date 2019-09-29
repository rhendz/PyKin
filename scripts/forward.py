import sys, getopt, bluetooth

sys.path.append('.')
import RTIMU
import os
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

bd_addr = "A8:7D:12:04:61:C0"

# Try to connect via Bluetooth
while True:
    ret = os.system("bluetoothctl connect ",bd_addr)
   
    if ret == 0:
        break

    time.sleep(10)

# Try to connect to the server
while True:
    try:
        sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((bd_addr,2))
        print "Passed!"
        break
    except:
        print "Trying to connect..."
        pass

while True:
  
    if imu.IMURead():

        data = imu.getIMUData()
        fusionPose = data["fusionPose"]
       
        sock.send("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]),
            math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))
        
        print("r: %f p: %f y: %f" % (math.degrees(fusionPose[0]),
            math.degrees(fusionPose[1]), math.degrees(fusionPose[2])))

        time.sleep(.500)

sock.close()
