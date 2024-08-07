import socket

ports = list(range(1, 65536))

def basic_syn_scan(host):
    print(f"Open ports at {host}:")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

host = "8.8.8.8"

if __name__ == "__main__":
    basic_syn_scan(host)
