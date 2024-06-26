import socket

def send_command(command):
    host = ''
    port = 8081
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        sock.connect((host, port))
        
        sock.sendall(command)
        
        response = sock.recv(4096)
        print('Received:', response.decode('utf-8'))
    
    finally:
        sock.close()

send_command(b'*1\r\n$4\r\nPING\r\n')
