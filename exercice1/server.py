import socket
import sys
import utils


def server(server_port=1235):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server ready...!")
    connection_socket, address = server_socket.accept()
    while True:
        message = utils.receive_message(connection_socket)
        response = message.decode('utf-8').upper().encode('utf-8')
        utils.send_message(connection_socket, response)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"options:\n"
              f"\t-p, --port port_address : set address port to connect\n"
              f"\tusage: --port 1235\n"
              f"\n"
              f"Notice: using default values : port=1235\n")
        server()
    else:
        port = 0
        if sys.argv[1] in ['-p', '--port']:
            port = int(sys.argv[2])
        else:
            print(f"options:\n"
                  f"\t-p, --port port_address : set address port to connect\n"
                  f"\tusage: --port 1235\n"
                  f"\n"
                  f"Notice: using default values : port=1235\n")
            server()
        server(server_port=port)
