#!/bin/bash

cmd_server="python3 server.py"
server_ip="127.0.0.1"
server_port=1235
cmd_proxy="python3 proxy_censeur.py"
proxy_ip="127.0.0.1"
proxy_port=1234
cmd_client="python3 client.py"


$cmd_server --port $server_port & $cmd_proxy --proxy $proxy_port --port $server_port --ip $server_ip & $cmd_client --port $proxy_port --ip $proxy_ip
