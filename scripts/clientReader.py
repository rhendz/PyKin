import bluetooth, json, os.path

# Set up for client to listen from server
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_sock.bind(("",2))
server_sock.listen(2)
client_sock,address = server_sock.accept()

# Constantly listens for input
while 1:

    # Checks and sees if GUI has read json file
    if not os.path.exists('log.json'):

        # If GUI has, make new file
        with open("log.json", "w") as f:
            buf = {}

            # Splice incoming data
            data = client_sock.recv(1024)
            data = data.split()
            buf['Roll'] = [data[1]]
            buf['Pitch'] = [data[3]]
            buf['Yaw'] = [data[5]]

            # Dumps into json file
            json.dump(buf, f)

client_sock.close()
server_sock.close()
