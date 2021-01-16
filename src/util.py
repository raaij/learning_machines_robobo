import socket

def get_ip_address():
    # https://stackoverflow.com/q/24196932
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
