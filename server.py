import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # AF_INET is connection through internet and SOCK_STREAM is TCP 
ip = input("IP Address :")
port = input("Port :")
server.bind((ip, int(port))) #ip and port should be same in both client and server
server.listen()

while True:
    print("server is waiting....")
    client,addr = server.accept()
    print("client connected from ", addr)

    while True:
        clt_msg = client.recv(1024)

        if clt_msg.decode('utf-8') == "end":
            break

        print("Client: %s" % clt_msg.decode('utf-8'))

        ser_msg = input("Server : ")
        client.send(ser_msg.encode("utf-8"))

    client.close()
server.close()
