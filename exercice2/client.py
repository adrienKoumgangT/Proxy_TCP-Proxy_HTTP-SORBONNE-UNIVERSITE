import socket
import utils


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
    s1 = message.split("<p>")
    s2 = s1[1].split("</p>")
    return s2[1]


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
