import socket
import utils
import sys


def form_request(r):
    if r["REQUEST"] == "POST":
        re = f"""POST {r["URI"]} HTTP/1.1
Type: {r["TYPE"]}
Content-Length: {r["CONTENT_LENGTH"]}

{r["DATA"]}"""
        return re
    elif r["REQUEST"] in ["GET", "DELETE"]:
        re = f"""{r["REQUEST"]} {r["URI"]} HTTP/1.1"""
        return re


def read_response(message):
    ls = message.split("\n\n")
    return {"HEAD": ls[0], "BODY": ls[1]}


def client(server_ip="127.0.0.1", server_port=1234):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    print("Client ready...!")
    mt = ""
    while mt != "EXIT":
        while mt not in ["GET", "POST", "DELETE"]:
            mt = input("Enter the method: ")
            mt = mt.upper()
        uri = input("Enter the uri: ")
        re = {"REQUEST": mt, "URI": uri}
        if mt == "POST":
            try:
                with open(uri) as f:
                    read_data = f.read()
                    re["CONTENT-LENGTH"] = len(read_data)
                    re["DATA"] = read_data
            except FileNotFoundError:
                print("File not found. please try again")
        message = form_request(re)
        utils.send_message(client_socket, message.encode('utf-8'))
        response = utils.receive_message(client_socket).decode('utf-8')
        rp = read_response(response)
        print(rp)
        mt = input("Enter the method: ")
        mt = mt.upper()
    utils.send_message(client_socket, mt.encode('utf-8'))
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
