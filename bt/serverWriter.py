import bluetooth

# This sends input from server to client
bd_addr = "34:E1:2D:DE:E0:85"
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, 2))

while 1:

    # Sends message to client
    msg = raw_input()
    sock.send(msg)
    if msg == 'stop':
        break

sock.close()
