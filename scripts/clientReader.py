import bluetooth, json, os.path

# Set up for client to listen from server
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)
client_sock,address = server_sock.accept()

# Constantly listens for input
while 1:
    # If GUI has, make new file
    #f = open('log.json', 'w')
    buf = {}
    
    # Splice incoming data
    data = client_sock.recv(1024)
    data = data.split()
    buf['Roll'] = [data[1]]
    buf['Pitch'] = [data[3]]
    buf['Yaw'] = [data[5]]

    print(data)
        
    # Dumps into json file
    with open("/home/ankush/github/hack2019/hack2019/src/assets/log.json", 'w') as f:
        json.dump(buf, f)

client_sock.close()
server_sock.close()
