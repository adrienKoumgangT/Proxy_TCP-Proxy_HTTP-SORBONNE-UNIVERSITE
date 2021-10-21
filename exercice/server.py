import sys
from xmlrpc.server import *


def my_function(message):
    return message.upper()


def server(server_port=1237):
    s = SimpleXMLRPCServer(('127.0.0.1', server_port))
    s.register_introspection_functions()
    s.register_multicall_functions()
    s.register_function(my_function)
    print("Server ready...!")
    s.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"options:"
              f"\t-p, --port port_address : set address port to connect"
              f"\tusage: --port 1235"
              f""
              f"Notice: using default values : port=1235")
        server()
    else:
        port = 0
        if sys.argv[1] in ['-p', '--port']:
            port = int(sys.argv[2])
        else:
            print(f"options:"
                  f"\t-p, --port port_address : set address port to connect"
                  f"\tusage: --port 1235"
                  f""
                  f"Notice: using default values : port=1235")
            server()
        server(server_port=port)
