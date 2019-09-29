import bluetooth

# Set up to listen to client
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",1))
server_sock.listen(1)
client_sock,address = server_sock.accept()

# Set up to send to client
"""
bd = "34:E1:2D:DE:E0:81"
c_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
c_sock.connect((bd,2))
"""

print "Accepted connection from ",address

while 1:

    """    # Sends data from server
    msg = raw_input()
    sock.send(msg)
    if msg == 'stop':
        break
    """
    # Reads data from client
    data = client_sock.recv(1024)
    print "received [%s]" % data
    if data == 'stop':
        break

client_sock.close()
server_sock.close()
