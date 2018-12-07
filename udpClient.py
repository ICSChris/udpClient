import socket

target_host = "127.0.0.1"
target_port = 2600

# Create a socket object and pass to the client variable
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Transmit a test packet
client.sendto(b"AAABBBCCC",(target_host,target_port))

# Receive data from the target server
data, addr = client.recvfrom(4096)

print(data)

