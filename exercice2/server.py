import socket
import utils
import pathlib
import datetime
import os

path_database = "./database/server/"


def read_message(message):
    if message[0] in ["G", "D"]:
        lm = message.split(" ")
        r = {"REQUEST": lm[0], "URI": lm[1], "PROTOCOL": lm[2]}
        return r
    elif message[0] == "P":
        ms = message.split("\n")
        lm = ms[0].split(" ")
        r = {"REQUEST": lm[0], "URI": lm[1], "PROTOCOL": lm[2],
             "TYPE": ms[1].split(" ")[1],
             "DATA": "\n".join(ms[3:])}
        return r
    else:
        return {}


def form_http_data(data, title="index"):
    r = f"""<!DOCTYPE>
<html>
    <head>
        <title>{title}</title>
    <head>
    <body>
        <p>{data}</data>
    </body>
</html>"""
    return r


def form_response(response):
    fhd = form_http_data(response["DATA"], response["FILE"])
    r = f"""{response["HTTP"]} {response["STATUS"]}
Server: Python/3.8.10
Date: {response["DATE"]}
Content-Type: {response["TYPE"]}
Content-length: {len(fhd)}

{fhd}"""
    return r


def search_file(filename):
    d = pathlib.Path(path_database)
    filename = filename.split("/")[-1]
    for file in d.rglob('*'):
        if file.is_file():
            path_name = str(file)
            name = path_name.split("/")[-1]
            if name == filename:
                return path_name
    return ""


def handle_post(request):
    uri = request["URI"].split("/")
    name_file = "-".join(uri)
    with open(path_database+name_file, "wb") as f:
        f.write(request["DATA"].encode('utf-8'))
    response = {"HTTP": request["HTTP"], "STATUS": "200 OK",
                "TYPE": "text/html", "FILE": name_file,
                "DATA": "OPERATION SUCCESS",
                "LENGTH": str(len("OPERATION SUCCESS")),
                "DATE": str(datetime.datetime.now())}
    return form_response(response)


def handle_get(request):
    filename = request["URI"].split("/")
    filename = "-".join(filename)
    file_request = search_file(filename)
    response = {"HTTP": request["HTTP"], "FILE": filename}
    if file_request:
        response["STATUS"] = "200 OK"
        response["TYPE"] = "text/html"
        try:
            with open(file_request, "rb") as file:
                content = file.read().decode('utf-8')
                response["DATA"] = content
                response["LENGTH"] = str(len(content))
        except FileNotFoundError:
            print("Error during open file request")
    else:
        response["STATUS"] = "ERROR 404"
        response["TYPE"] = "text/html"
        response["DATA"] = "File Not Found"
        response["LENGTH"] = str(len("File Not Found"))
    response["DATE"] = str(datetime.datetime.now())
    return form_response(response)


def handle_delete(request):
    filename = request["URI"].split("/")
    filename = "-".join(filename)
    file_request = search_file(filename)
    response = {"HTTP": request["HTTP"], "FILE": filename}
    if file_request:
        response["STATUS"] = "200 OK"
        response["TYPE"] = "text"
        response["DATA"] = "File Delete"
        response["LENGTH"] = str(len("File Delete"))
        os.remove(file_request)
    else:
        response["STATUS"] = "ERROR 404"
        response["TYPE"] = "text"
        response["DATA"] = "File Not Found"
        response["LENGTH"] = str(len("File Not Found"))
    response["DATE"] = str(datetime.datetime.now())
    return form_response(response)


def server(server_port=1235):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    print("Server ready...!")
    connection_socket, address = server_socket.accept()
    while True:
        message = utils.receive_message(connection_socket).decode('utf-8')
        msg = read_message(message)
        if msg["REQUEST"] == "POST":
            response = handle_post(msg)
        elif msg["REQUEST"] == "GET":
            response = handle_get(msg)
        elif msg["REQUEST"] == "DELETE":
            response = handle_delete(msg)
        else:
            response = "BAD REQUEST"
        utils.send_message(connection_socket, response.encode('utf-8'))


if __name__ == '__main__':
    server()
