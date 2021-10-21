import socket
import threading
import sys
import utils


def handle_client(socket_server, socket_client):
    message_client = utils.receive_message(socket_client)
    while message_client.decode('utf-8') != "exit":
        utils.send_message(socket_server, message_client)
        message_server = utils.receive_message(socket_server)
        utils.send_message(socket_client, message_server)
        message_client = utils.receive_message(socket_client)
    socket_client.close()


def proxy(proxy_port=1234, server_ip="127.0.0.1", server_port=1235):
    # création de socket de connection avec le serveur
    proxy_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_client_socket.connect((server_ip, server_port))
    # création de socket de connection avec les clients
    proxy_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_server_socket.bind(('', proxy_port))
    proxy_server_socket.listen(5)
    print("Proxy ready...!")
    print()
    while True:
        connection_socket, address = proxy_server_socket.accept()
        threading.Thread(target=handle_client, args=(proxy_client_socket, connection_socket, )).start()


if __name__ == '__main__':
    if len(sys.argv) != 7:
        print(f"options:"
              f"\t-o, --proxy port_proxy : set address port of proxy"
              f"\t-i, --ip ip_address : set address ip to connect"
              f"\t-p, --port port_address : set address port to connect"
              f"\tusage: --proxy 1234 --ip 127.0.0.1 --port 1235"
              f""
              f"Notice: using default values : proxy=1234 ip=127.0.0.1 port=1235")
        proxy()
    else:
        a_ip = ""
        a_port = 0
        p_port = 0
        for i in range(1, 5, 2):
            if sys.argv[i] in ['-i', '--ip']:
                a_ip = sys.argv[i + 1]
            elif sys.argv[i] in ['-p', '--port']:
                a_port = int(sys.argv[i + 1])
            elif sys.argv[i] in ['-o', '--proxy']:
                p_port = int(sys.argv[i+1])
            else:
                print(f"options:"
                      f"\t-o, --proxy port_proxy : set address port of proxy"
                      f"\t-i, --ip ip_address : set address ip to connect"
                      f"\t-p, --port port_address : set address port to connect"
                      f"\tusage: --proxy 1234 --ip 127.0.0.1 --port 1235"
                      f""
                      f"Notice: using default values : proxy=1234 ip=127.0.0.1 port=1235")
                proxy()
        proxy(proxy_port=p_port, server_ip=a_ip, server_port=a_port)
