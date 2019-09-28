# Uses Bluez for Linux
#
# sudo apt-get install bluez python-bluez
# 
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/x232.html
# Taken from: https://people.csail.mit.edu/albert/bluez-intro/c212.html

import bluetooth

# This is the general interface we implement into each client/server

RASP_BLUE_MAC = "B8:27:EB:41:5D:74"

def receiveMessages():
  server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  
  port = 1
  server_sock.bind(("",port))
  server_sock.listen(1)
  
  client_sock,address = server_sock.accept()
  print "Accepted connection from " + str(address)
  
  data = client_sock.recv(1024)
  print "received [%s]" % data
  
  client_sock.close()
  server_sock.close()
  
def sendMessageTo(targetBluetoothMacAddress):
  port = 1
  sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
  sock.connect((targetBluetoothMacAddress, port))
  sock.send("hello!!")
  sock.close()
