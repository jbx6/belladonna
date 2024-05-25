import datetime
import socket

HOST = "192.168.2.2"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        with open("data.csv", "a") as data_file:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(data)
                temperature, humidity, pressure = data.decode("utf-8").split(",")
                time = datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S")

                #print(f"Temperature: {temperature}, Humidity: {humidity}, Pressure: {pressure}")

                newData = f"{time},{temperature},{humidity},{pressure}\n"

                data_file.write(newData)
                data_file.flush()
                print(f"Received data: \n{data.decode('utf-8')}")