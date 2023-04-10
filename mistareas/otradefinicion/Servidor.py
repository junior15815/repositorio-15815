import socket

# Configuración del servidor
HOST = 'localhost'
PORT = 8000

# Creación del socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asociación del socket con el host y puerto especificados
server_socket.bind((HOST, PORT))

# Espera de una conexión entrante
server_socket.listen()

print(f'Servidor escuchando en {HOST}:{PORT}')

# Manejo de conexiones entrantes
while True:
    # Aceptación de la conexión entrante
    client_socket, address = server_socket.accept()
    print(f'Conexión entrante desde {address}')

    # Recepción de datos del cliente
    data = client_socket.recv(1024)
    print(f'Datos recibidos: {data.decode()}')

    # Envío de datos al cliente
    message = 'Hola cliente!'
    client_socket.send(message.encode())

    # Cierre de la conexión con el cliente
    client_socket.close()
