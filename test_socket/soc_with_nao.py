import socket

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
serv_sock.bind(('', 53210))
serv_sock.listen(10)

while (True):
    client_sock, client_addr = serv_sock.accept()
    print('connected by: ', client_addr)
    while True:
        data = client_sock.recv(1024)
        print('read data')
        if not data:
            break
        client_sock.sendall(data)
    client_sock.close()


