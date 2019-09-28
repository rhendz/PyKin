import bluetooth

bd_addr = "B8:27:EB:41:5D:74"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

while 1:
    msg = raw_input()

    if msg == 'stop':
        break

    sock.send(msg)

sock.close()
