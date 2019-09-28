import bluetooth

bd_addr = "B8:27:EB:41:5D:74"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")
data = sock.recv(1024)
print "received [%s]" % data

sock.close()
