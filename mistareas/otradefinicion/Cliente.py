import socket

# Configuración del cliente
HOST = 'localhost'
PORT = 8000

# Creación del socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexión con el servidor
client_socket.connect((HOST, PORT))

# Envío de datos al servidor
message = 'Hola servidor!'
client_socket.send(message.encode())

# Recepción de datos del servidor
data = client_socket.recv(1024)
print(f'Datos recibidos: {data.decode()}')

# Cierre del socket del cliente
client_socket.close()
