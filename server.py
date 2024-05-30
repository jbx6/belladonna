import datetime
import socket
import config

HOST = config.HOST
PORT = config.PORT

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}\n")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            with open("data.csv", "a") as data_file:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    # print(data) // 'debugging'
                    print(f"Received data: {data.decode('utf-8')} [temp, humidity, pressure] from {addr}")
                    try:
                        temperature, humidity, pressure = data.decode("utf-8").split(",")
                        time = datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S")

                        newData = f"{time},{temperature},{humidity},{pressure}"
                        data_file.write(newData + "\n")
                        data_file.flush()
                        print(f"Data saved: {newData} to data.csv\n")
                    except ValueError:
                        print("Received malformed data")
    print("Connection closed")