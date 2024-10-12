import socket
from dotenv import load_dotenv, dotenv_values

load_dotenv()
SERVER_PORT = int(dotenv_values('.env')['SERVER_PORT'])

socket_server = socket.socket()
print('Successfully connect to the socket connection')

socket_server.bind(('', SERVER_PORT))
print(f"server bind to the {SERVER_PORT}")

socket_server.listen(2)
print(f"server listening to {2} clients")