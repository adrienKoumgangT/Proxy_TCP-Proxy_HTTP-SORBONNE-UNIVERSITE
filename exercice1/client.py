import socket
import utils


def client(server_ip="127.0.0.1", server_port=1234):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Client ready...!")
    print("Enter 'exit' for close.")
    print()
    message = input("input text: ")
    while message != "exit":
        utils.send_message(client_socket, message.encode('utf-8'))
        response = utils.receive_message(client_socket).decode('utf-8')
        print(response)
        message = input("input text: ")
    utils.send_message(client_socket, message.encode('utf-8'))
    client_socket.close()


if __name__ == '__main__':
    client()
