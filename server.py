import asyncio


# https://docs.python.org/3/library/asyncio-protocol.html
class ClientServerProtocol(asyncio.Protocol):
    """ A Server Protocol listening for messages """

    def __init__(self):
        self.transport = None

    def connection_made(self, transport):
        """ Called when connection is initiated """

        self.transport = transport

        # 'peername': the remote address to which the socket is connected,
        # result of socket.socket.getpeername() (None on error)
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))

    def data_received(self, data):

        message = data.decode()
        print('Data received: {!r}'.format(message))
        resp = self.process_data(message)

        print('Send: {!r}'.format(resp))
        try:
            self.transport.write(("b"+resp).encode("utf-8"))

            print('Close the client socket')
            self.transport.close()
        except:
            raise ClientProtocolError

    def process_data(self, data):
        return f"---{data}----"


class ClientSocketError:
    pass


class ClientProtocolError:
    pass


def run_server(host, port):
    loop = asyncio.get_event_loop()

    # Each client will create a new protocol instance
    try:
        coro = loop.create_server(ClientServerProtocol, host, port)
    except:
        raise ClientSocketError()

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    try:
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.close()
    except:
        pass


if __name__ == "__main__":
    run_server('127.0.0.1', 8181)
