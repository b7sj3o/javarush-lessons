import socket
# Створюємо сокет TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Підключаємося до сервера
host = 'localhost'
port = 12345
client_socket.connect((host, port))
# Відправляємо дані на сервер
message = "Hello, server!"
client_socket.sendall(message.encode())
# Отримуємо відповідь від сервера
data = client_socket.recv(1024).decode()
print(f"Получено от сервера: {data}")
# Закриваємо з'єднання
client_socket.close()