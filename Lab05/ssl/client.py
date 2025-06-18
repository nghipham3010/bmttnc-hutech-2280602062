import socket
import ssl
import threading

# Thông tin server
server_address = ('localhost', 2062)

def receive_data(ssl_socket):
    try:
        while True:
            data = ssl_socket.recv(1024)
            if not data:
                break
            print("Nhận:", data.decode('utf-8'))
    except:
        pass
    finally:
        ssl_socket.close()
        print("Kết nối đã đóng.")

try:
    # Tạo socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Tạo SSL context cho client
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Bỏ kiểm tra chứng chỉ (không khuyến khích dùng trong thực tế)

    # Thiết lập kết nối SSL
    ssl_socket = context.wrap_socket(client_socket, server_hostname='localhost')
    ssl_socket.connect(server_address)

    # Bắt đầu thread để nhận dữ liệu từ server
    receive_thread = threading.Thread(target=receive_data, args=(ssl_socket,))
    receive_thread.start()

    # Gửi dữ liệu từ bàn phím
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        ssl_socket.send(message.encode('utf-8'))

    ssl_socket.close()
except Exception as e:
    print("Lỗi:", e)
