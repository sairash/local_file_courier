import socket
import os ,os.path
import argparse


parser = argparse.ArgumentParser(description="Simple File Sender")
parser.add_argument("-f","--file", help="File name to send")
parser.add_argument("-ho", "--host", help="The host/IP address of the receiver")
parser.add_argument("-p", "--port", help="Port to use, default is 5001", default=5001)
args = parser.parse_args()
filepath = args.file
host = args.host
port = args.port


CHUNKSIZE = 1_000_000

# Make a directory for the received files.
main_path = os.path.join(filepath, 'localCourier') 
os.makedirs(main_path,exist_ok=True)
print(main_path)

BUFFER_SIZE = 4096


sock = socket.socket()
sock.connect((host,int(port)))

DIR = 'localCourier'
numberOfFiles = len(os.listdir(main_path))+1
print(numberOfFiles)

with sock,sock.makefile('rb') as clientfile:
    while True:
        raw = clientfile.readline()
        if not raw: break # no more files, server closed connection.

        filename = raw.strip().decode()
        length = int(clientfile.readline())
        print(f'Downloading {filename}...\n  Expecting {length:,} bytes...',end='',flush=True)

        path = os.path.join(filepath+'\\localCourier\\version_'+str(numberOfFiles),filename)
        # print()
        paths_array=path.split('..\\')
        new_path = paths_array.join('')
        os.makedirs(os.path.dirname(new_path),exist_ok=True)

        # Read the data in chunks so it can handle large files.
        with open(new_path,'wb') as f:
            while length:
                chunk = min(length,CHUNKSIZE)
                data = clientfile.read(chunk)
                if not data: break
                f.write(data)
                length -= len(data)
            else: # only runs if while doesn't break and length==0
                print('Complete')
                continue

        # socket was closed early.
        print('Incomplete')
        break 
