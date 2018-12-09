# asyncio, tcp client
import asyncio


class Client:
    """
    Инкапсуляция соединения с сервером, клиентский сокет и
    методы для получения и отправки метрик на сервер
    """

    def __init__(self, addr, port, timeout=None):
        self.addr = addr
        self.port = port
        self.timeout = timeout

    async def tcp_client(message, loop):
        reader, writer = await asyncio.open_connection("127.0.0.1", 10001, loop=loop)
        print("send: %r" % message)
        writer.write(message.encode())
        writer.close()

    def put(self, metric, value, timestamp):
        return

    def get(self, metric):
        return


# except ClientError:

def _main():
    client = Client("127.0.0.1", 8888, timeout=15)

    loop = asyncio.get_event_loop()
    message = "Hello, Asyncio!"
    loop.run_until_complete(client.tcp_client(message, loop))
    loop.close()

    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 0.5, timestamp=1150864248)

    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)

    print(client.get("*"))


if __name__ == "__main__":
    _main()

