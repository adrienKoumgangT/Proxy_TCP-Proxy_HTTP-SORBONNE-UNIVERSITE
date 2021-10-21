import socket
import utils
import sys


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
    if len(sys.argv) != 5:
        print(f"options:"
              f"\t-i, --ip ip_address : set address ip to connect"
              f"\t-p, --port port_address : set address port to connect"
              f"\tusage: --ip 127.0.0.1 --port 1234"
              f""
              f"Notice: using default values : ip=127.0.0.1 port=1234")
        client()
    else:
        a_ip = ""
        a_port = 0
        for i in range(1, 5, 2):
            if sys.argv[i] in ['-i', '--ip']:
                a_ip = sys.argv[i + 1]
            elif sys.argv[i] in ['-p', '--port']:
                a_port = int(sys.argv[i + 1])
            else:
                print(f"options:"
                      f"\t-i, --ip ip_address : set address ip to connect"
                      f"\t-p, --port port_address : set address port to connect"
                      f"\tusage: --ip 127.0.0.1 --port 1234"
                      f""
                      f"Notice: using default values : ip=127.0.0.1 port=1234")
                client()
        client(server_ip=a_ip, server_port=a_port)
