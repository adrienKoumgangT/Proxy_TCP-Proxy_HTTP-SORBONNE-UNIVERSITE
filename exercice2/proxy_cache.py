import socket
import threading
import utils


path_database = "./database/proxy/"


def search_file(filename):
    try:
        with open(path_database+filename, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return b''


def write_file(filename, content):
    try:
        with open(path_database+filename, "wb") as f:
            f.write(content)
    except FileNotFoundError as e:
        print(e)


def handle_client(socket_server, socket_client):
    message_client = utils.receive_message(socket_client)
    while message_client.decode('utf-8') != "exit":
        lm = message_client.split("\n")
        head = lm[0].split(" ")
        if head[0] == "GET":
            uri = head[1].split("/")
            file_name = "-".join(uri)
            content = search_file(file_name)
            if content:
                utils.send_message(socket_client, content)
            else:
                utils.send_message(socket_server, message_client)
                message_server = utils.receive_message(socket_server)
                write_file(file_name, message_server)
                utils.send_message(socket_client, message_server)
        else:
            utils.send_message(socket_server, message_client)
            message_server = utils.receive_message(socket_server)
            utils.send_message(socket_client, message_server)
        message_client = utils.receive_message(socket_client)
    socket_client.close()


def proxy(proxy_port=1234, server_ip="127.0.0.1", server_port=1235):
    proxy_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_client_socket.connect((server_ip, server_port))
    proxy_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server_socket.bind(('', proxy_port))
    proxy_server_socket.listen(5)
    print("Proxy ready...!")
    print()
    while True:
        connection_socket, address = proxy_server_socket.accept()
        threading.Thread(target=handle_client, args=(proxy_client_socket, connection_socket, )).start()


if __name__ == '__main__':
    proxy()
