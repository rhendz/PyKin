import bluetooth

# Set up for client to listen from server
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)
client_sock,address = server_sock.accept()

print "Accepted connection from ",address

while 1:

    # Reads data from server
    data = client_sock.recv(1024)
    print "received [%s]" % data
    if data == 'stop':
        break

client_sock.close()
server_sock.close()
