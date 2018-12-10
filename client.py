import socket
import time


class Client:
    """
    Инкапсуляция соединения с сервером, клиентский сокет и
    методы для получения и отправки метрик на сервер
    """

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        # self.sock.close()

    # Метод put не возвращает ничего в случае успешной отправки и выбрасывает исключение ClientError в случае неуспешной.
    def put(self, metric, value, timestamp):
        try:
            if timestamp is None:
                timestamp = str((int(time.time())))

            message = f"put {metric} {float(value)} {timestamp}\n"
            self.sock.send(message.encode("utf-8"))

            data = self.sock.recv(1024).decode().split("\n")  # Server answer

            if data[0] is not "ok":
                raise ClientError

        except socket.timeout:
            raise ClientError

    def get(self, metric):
        try:
            message = f"get {metric}\n"
            self.sock.send(message.encode("utf-8"))

            data = ""
            while True:
                data += self.sock.recv(1024).decode()  # Server answer
                if "\n\n" in data:
                    break
                answer = (data[3::]).split()  # Получился список
                return self.get_dict(answer)

        except socket.timeout:
            raise ClientError

    def get_dict(self, data):
        ans_dict = dict()

        for i, key in enumerate(data[::3]):
            if key in ans_dict:
                ans_dict[key].append(tuple([int(data[i * 3 + 1]), float(data[i * 3 + 2])]))
            else:
                ans_dict.update({key: [tuple([int(data[i * 3 + 1]), float(data[i * 3 + 2])])]})
        return ans_dict

    def close(self):
        return self.sock.close()


# except ClientError:
class ClientError(Exception):
    pass


# def _main():
#     client = Client("127.0.0.1", 8888, timeout=15)
#
#     client.put("palm.cpu", 0.5, timestamp=1150864247)
#     client.put("palm.cpu", 2.0, timestamp=1150864248)
#     client.put("palm.cpu", 0.5, timestamp=1150864248)
#
#     client.put("eardrum.cpu", 3, timestamp=1150864250)
#     client.put("eardrum.cpu", 4, timestamp=1150864251)
#     client.put("eardrum.memory", 4200000)
#
#     print(client.get("*"))
#
#
# if __name__ == "__main__":
#     _main()
