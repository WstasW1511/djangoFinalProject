# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("", 9090))
# sock.listen(1)
# client = []
# print("Server is running, press CTRL+C to stop")
#
# while True:
#     conn, addres = sock.accept()
#     data = conn.recv(1024)
#     print(addres[0], addres[1])
#     if addres not in client:
#         client.append(addres)  # Если такого клиента нету , то добавить
#         for clients in client:
#             # if clients == addres:
#             #     continue  # Не отправлять данные клиенту, который их прислал
# #             sock.sendto(data, clients)
# import socket
#
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind(("", 9090))
# sock.listen(1)
# print("Server is running, press CTRL+C to stop")
#
# while True:
#     conn, addr = sock.accept()
#     data=conn.recv(1024)
#     conn.send(data)
#     print(data)
#     print(conn)
#     print(addr)

#
# import time, socket, sys
#
# new_socket = socket.socket()
# host_name = socket.gethostname()
# s_ip = socket.gethostbyname(host_name)
# port = 8080
# new_socket.bind((host_name, port))
# print("Binding successful!")
# print("This is your IP: ", s_ip)
# name = input('Enter name: ')
# new_socket.listen(1)
# conn, add = new_socket.accept()
# print("Received connection from ", add[0])
# print('Connection Established. Connected From: ', add[0])
# client = (conn.recv(1024)).decode()
# print(client + ' has connected.')
# conn.send(name.encode())
#
# while True:
#     message = input('Me : ')
#     conn.send(message.encode())
#     message = conn.recv(1024)
#     message = message.decode()
#     print(client, ':', message)





import socket


def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client
    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()