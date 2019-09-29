import bluetooth

# Connection set for client to server
bd_addr = "B8:27:EB:41:5D:74"
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, 1))

while 1:

    # Sends message to server
    msg = raw_input()
    sock.send(msg)
    if msg == 'stop':
        break

sock.close()
