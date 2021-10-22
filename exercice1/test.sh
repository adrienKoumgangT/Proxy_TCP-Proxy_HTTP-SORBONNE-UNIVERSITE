#!/bin/bash

cmd_server="python3 server.py"

cmd_proxy="python3 proxy.py"

cmd_client="python3 client.py"

#lance l'exécution du server et du client
$cmd_server & $cmd_proxy & $cmd_client && fg
