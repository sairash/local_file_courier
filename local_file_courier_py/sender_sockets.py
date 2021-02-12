import socket
import os
import argparse


parser = argparse.ArgumentParser(description="Simple File Sender")
parser.add_argument("-f","--file", help="File name to send")
parser.add_argument("-p", "--port", help="Port to use, default is 5001", default=5001)
args = parser.parse_args()
filepath = args.file
port = args.port





def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)

    return total_size

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
print(local_ip)
print(f"File Path {filepath}.. & Port {port}.. Local Ip {local_ip}")

CHUNKSIZE = 1_000_000

sock = socket.socket()
sock.bind((local_ip,int(port)))
sock.listen(1)
total_folder_size=int(get_size(filepath))


while True:
    print('Waiting for a client...')
    client,address = sock.accept()
    print(f'Client joined from {address}')
    with client:
        for path,dirs,files in os.walk(filepath):
            for file in files:
                filename = os.path.join(path,file)
                relpath = os.path.relpath(filename,'server')
                filesize = os.path.getsize(filename)

                print(f'Sending {relpath}')

                with open(filename,'rb') as f:
                    client.sendall(relpath.encode() + b'\n')
                    client.sendall(str(filesize).encode() + b'\n')

                    # Send the file in chunks so large files can be handled.
                    while True:
                        data = f.read(CHUNKSIZE)
                        if not data: break
                        client.sendall(data)
        print('Done.')