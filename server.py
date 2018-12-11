import asyncio


# https://docs.python.org/3/library/asyncio-protocol.html
class ClientServerProtocol(asyncio.Protocol):

    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        self.transport = transport

        # 'peername': the remote address to which the socket is connected,
        # result of socket.socket.getpeername() (None on error)
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))
        resp = self.process_data(message)

        print('Send: {!r}'.format(message))
        self.transport.write(resp.encode())

        print('Close the client socket')
        self.transport.close()

    def process_data(self, data):
        return True


class ClientSocketError:
    pass


class ClientProtocolError:
    pass


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server('127.0.0.1', 8181)
