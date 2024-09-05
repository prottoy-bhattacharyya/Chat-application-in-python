import socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',12345))
server.listen(5)

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