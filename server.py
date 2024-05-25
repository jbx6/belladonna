import socket

HOST = "0.0.0.0"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        with open("datalog.txt", "a") as data_file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                data_file.write(data.decode("utf-8"))
                data_file.flush()
                print(f"Received data: {data.decode('utf-8')}")