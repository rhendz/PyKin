CC=gcc

all: rfcomm-client rfcomm-server

%: %.c
	$(CC) -c $@ $<

rfcomm-client: rfcomm-client.o
	$(CC) -o rfcomm-client rfcomm-client.o -lbluetooth

rfcomm-server: rfcomm-server.o
	$(CC) -o rfcomm-server rfcomm-server.o -lbluetooth
