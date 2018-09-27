import socket
import crypto.cipher AES
From crypto.publiKey import RSA
From crypto import random
HOST, PORT = 'localhost', 8080

def main():
    listen_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    listen_socket.bind((HOST, PORT))
    listen_socket.listen(1)  
    while True:
        client_connection, client_address = listen_socket.accept()
        
        
    # this is my change hi

        client_connection.send(response)
    client_connection.close()

main()