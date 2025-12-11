Dependencies:
Bash
Netcat
sudo apt install netcat


A lightweight Bash script that performs a TCP port scan on a target IP or hostname using Netcat (nc). 
The script interactively asks for the target and port range, then checks each port and prints whether it is open or closed.


Usage:
chmod +x portscan.sh
./portscan.sh

Enter the target and port range when prompted
