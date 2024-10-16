import socket
from dotenv import load_dotenv, dotenv_values
import argparse

load_dotenv()
server_port = int(dotenv_values('.env')['SERVER_PORT'])

def server(clientNumber=3, alwaysRun=True):
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    print('socket is ready')
    
    server_socket.bind(('', server_port))
    server_socket.listen(clientNumber)
    print(f'socket is bind in port : {server_port}, listen to {clientNumber}')
    
    if alwaysRun:
        global Run
        Run = True
        try:
            while Run:
                client, add = server_socket.accept()
                print(f'got connection from {add}')
                
                client.send('you are connected'.encode())
                
        except KeyboardInterrupt:
            server_socket.close()
            print('server has been shutdown')
            Run = False
    
    else:
        client, add = server_socket.accept()
        print(f'connected with {add}')
        client.send('you are connected'.encode())
        
        client.close()


parser = argparse.ArgumentParser()
parser.add_argument(
    "--clientnumber",
    help="client number of server to listened for",
    type=int,
    default=3
)

parser.add_argument(
    "--isAlwaysRun",
    help="client number of server to listened for",
    type=bool,
    default=True
)

args = parser.parse_args()

if __name__ == '__main__':
    print(args.clientnumber, args.isAlwaysRun)
    server(
        clientNumber=args.clientnumber,
        alwaysRun=args.isAlwaysRun
    )