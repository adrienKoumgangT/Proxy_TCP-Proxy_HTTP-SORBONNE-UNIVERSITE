#!/bin/bash

cmd_server="python3 server.py"
server_ip="127.0.0.1"
server_port=1235
cmd_proxy="python3 proxy.py"
proxy_ip="127.0.0.1"
proxy_port=1234
cmd_client="python3 client.py"

exec 3<inputfile
exec 4>outputfile
exec 5>errorfile
# lecture du fichier de input (je mets chaque ligne dans l'array A)
i=0
# shellcheck disable=SC2162
while read -u 3 linea; do
  A[$i]=$linea
done

#lance l'exécution du server
$cmd_server --port $server_port;

#lance l'exécution du proxy
$cmd_proxy --proxy 1234 --port 1235 --ip $server_ip 2>&5;

#lance l'exécution en parallèle de plusieur client
for((j=1; j<i; j+=1)); do
  $cmd_client --ip $proxy_ip --port $proxy_port < "${A[$j]}" "exit" 1>&4 2>&5;
  $cmd_client --ip $proxy_ip --port $proxy_port < "${A[$j+1]}" "exit" 1>&4 2>&5;
done
