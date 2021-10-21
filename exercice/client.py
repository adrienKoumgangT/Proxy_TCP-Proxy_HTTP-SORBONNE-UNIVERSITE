import sys
from xmlrpc.client import *


def client(server_ip="127.0.0.1", server_port=1237):
    proxy = ServerProxy('http://'+server_ip+":"+str(server_port))
    message = ""
    while message != "exit":
        message = input("Enter sentence: ")
        print(proxy.my_function(message))


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
