import socket
import utils


def server(server_port=1235):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server ready...!")
    connection_socket, address = server_socket.accept()
    while True:
        message = utils.receive_message(connection_socket)
        message = message.decode('utf-8').upper().encode('utf-8')
        utils.send_message(connection_socket, message)


if __name__ == '__main__':
    server()
