import socket
import sys
import select

def telnet_data(data):
    print("Enter")
    print(f"Telnet data {data}")
    
    # Create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print("Connect to the server",sock)
        # Connect to the server
        sock.connect(("tp1.itrackrtd.co.in", 9004))
        sock.setblocking(False)
    except Exception as e:
        print(f"Failed to connect: {e}")
        return
    
    try:
        # Send data
        sock.sendall(data.encode('utf-8'))
        
        while True:
            read_sockets, _, _ = select.select([sock, sys.stdin], [], [])
            
            for s in read_sockets:
                if s == sock:
                    response = sock.recv(4096)
                    if not response:
                        print("Connection closed by the server.")
                        return
                    print(f"<<< {response.decode('utf-8')}")
                
                elif s == sys.stdin:
                    user_input = sys.stdin.read(4096)
                    if user_input:
                        sock.sendall(user_input.encode('utf-8'))
                        print(f">>> {user_input.strip()}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        sock.close()

# Example usage:
# telnet_data("test;")
