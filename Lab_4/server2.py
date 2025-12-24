import socket

HOST = "127.0.0.1"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print("Сервер очікує на клієнтів (Ctrl+C для виходу)...")

    while True:  # Цикл для постійної роботи
        conn, addr = s.accept()
        with conn:
            print(f"Обслуговуємо клієнта: {addr}")
            data = conn.recv(1024)
            if data:
                conn.sendall(data)