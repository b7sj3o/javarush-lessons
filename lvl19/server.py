import socket

# Створюємо сокет TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Прив'язуємо сокет до адреси та порту
host = 'localhost'
port = 12345

server_socket.bind((host, port))
# Починаємо прослуховування
server_socket.listen()
print(f"Сервер слушает на {host}:{port}")
while True:
# Приймаємо з'єднання
    client_socket, addr = server_socket.accept()
    print(f"Подключение от {addr}")
    # Отримуємо дані від клієнта
    data = client_socket.recv(1024).decode()
    print(f"Получено: {data}")
    # Надсилаємо відповідь
    response = f"Вы сказали: {data}"
    client_socket.sendall(response.encode())
    # Закриваємо з'єднання
    client_socket.close()