import yaml
import socket

config = yaml.safe_load(open('./config.yml'))

base = config['IP']['base']
port_from = config['PORT']['from']
port_to = config['PORT']['to']

ipAddresses = []
port_range = [port for port in range(port_from, port_to)]

for ip in range(0, 256):
    ipAddresses.append(f'{base}{ip}')

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for ip in ipAddresses:
        try:
            con = s.connect((ip, port))
            data = f'On host {ip}, port {port} is open!'
            print(data)
            write_csv(data)
            con.close()
        except:
            pass

def write_csv(data):
    with open('output.txt', 'a') as output:
        output.write(data)

if __name__ == "__main__":
    for port in port_range:
        port_scanner(port)