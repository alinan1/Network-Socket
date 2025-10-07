# Network Socket Programming Project Description
Python TCP client–server system built for Rutgers CS 352: Internet Technology.  
Demonstrates creating sockets, establishing a TCP connection, exchanging messages, and verifying traffic with Wireshark packet captures. 

# How It Works
1. Server.py binds to a a given TCP port and listens.
2. Client.py connects to the server’s IP + port.
3. The client sends lines of text, and the server reverses each line and swaps letter cases before sending the response back.
4. Traffic is captured in `.pcap` and inspected in Wireshark (handshake, payload, etc.).
