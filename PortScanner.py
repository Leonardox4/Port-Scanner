#!/bin/bash
read -p "Enter target IP or hostname: " TARGET
read -p "Enter start port: " START
read -p "Enter end port: " END

echo
echo "Scanning $TARGET from port $START to $END..."
echo

for ((port=$START; port<=$END; port++)); do
    nc -z -w 1 $TARGET $port 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "[OPEN]   TCP $port"
    else
        echo "[CLOSED] TCP $port"
    fi
done

echo
echo "Scan complete!"
