import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET is connection through internet and SOCK_STREAM is TCP
ip = input("IP Address :")
port = input("Port :")
client.connect((ip, int(port))) 

while True:
    clt_msg = input('enter msg :')
    client.send(clt_msg.encode('utf-8'))

    ser_msg = client.recv(1024)
    print("Server : " + ser_msg.decode('utf-8'))

    if str(ser_msg) == "end" : 
        break
client.close()
