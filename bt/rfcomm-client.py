import bluetooth

# Connection set up for the server (the Pi)
bd_addr = "B8:27:EB:41:5D:74"
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, 1))

""""
# Connection to listen to the server
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)
"""

#sever_client, address = server_sock.accept()
#print "Accepted connection from ",address

while 1:

    """    #Reads message
    data = server_client.recv(1024)
    print "Server said: %s" % data
    if data == 'stop':
        break
    """
    # Sends message
    msg = raw_input()
    sock.send(msg)
    if msg == 'stop':
        break

sock.close()
#server_sock.close()
#sever_client.close()
