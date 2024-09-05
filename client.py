import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',12345))

while True:
    clt_msg = input('enter msg :')
    client.send(clt_msg.encode('utf-8'))

    ser_msg = client.recv(1024)
    print("Server : " + ser_msg.decode('utf-8'))

    if str(ser_msg) == "end" : 
        break
client.close()
