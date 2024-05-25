import datetime
import socket

HOST = "192.168.2.2"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        with conn:
            with open("data.csv", "a") as data_file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # print(data) // 'debugging'
                    print(f"Received data: \n{data.decode('utf-8')}")
                    try:
                        temperature, humidity, pressure = data.decode("utf-8").split(",")
                        time = datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S")

                        newData = f"{time},{temperature},{humidity},{pressure}\n"
                        data_file.write(newData)
                        data_file.flush()
                        print(f"Data saved: {newData}")
                    except ValueError:
                        print("Received malformed data")
    print("Connection closed")