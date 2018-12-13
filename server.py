import asyncio
import re
import os
import tempfile
import json


class ClientError(Exception):
    """Общий класс исключений клиента"""
    pass


class ClientSocketError(ClientError):
    """Исключение, выбрасываемое клиентом при сетевой ошибке"""
    pass


class ClientProtocolError(ClientError):
    """Исключение, выбрасываемое клиентом при ошибке протокола"""
    pass


# https://docs.python.org/3/library/asyncio-protocol.html
class ClientServerProtocol(asyncio.Protocol):
    """ A Server Protocol listening for messages """

    def __init__(self):
        self.transport = None
        self.storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
        # print(self.storage_path)

        if not os.path.exists(self.storage_path):
            with open(self.storage_path, "w", encoding='utf-8') as f:
                f.write("{}")

    def connection_made(self, transport):
        """ Called when connection is initiated """

        self.transport = transport

        # 'peername': the remote address to which the socket is connected,
        # result of socket.socket.getpeername() (None on error)
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))

    def data_received(self, data):

        message = data.decode().lower()
        print('Data received: {!r}'.format(message))
        resp = self.process_data(message)

        try:
            print('Send: {!r}'.format(resp))
            self.transport.write((resp).encode("utf-8"))
            print('Close the client socket')
            self.transport.close()
        except:
            raise ClientProtocolError

    def process_data(self, data):
        data_list = data.split()
        # if data_list[0] in ["put", "get"]:
        if self.check_data(data_list):
            resp = "ok\n\n"
        else:
            resp = "error\nwrong command\n\n"
        return resp

    def check_data(self, data_list):
        code = False

        if len(data_list) > 1:  # put, get имееют от одного до трех параметров
            if data_list[0] == "put" and len(data_list) > 2:
                code = self.check_re(data_list[1], r'\w+\.\w+') and \
                       self.check_re(data_list[2], r'\d+\.?\d*')
                if code:
                    args = [data_list[1], data_list[2], ""]

                if len(data_list) > 3:
                    code = code and self.check_re(data_list[3], r'\d+')
                if code:
                    args = [data_list[1], data_list[2], data_list[3]]
                self.put(args[0], args[1], args[2])
            elif data_list[0] == "get":
                code = data_list[1] == '*' or \
                       self.check_re(data_list[1], r'\w+\.\w+')
        return code

    def check_re(self, source, regex):
        result = re.search(regex, source)
        return result and len(source) == len(result.group(0))

    def get_data(self):
        with open(self.storage_path, 'r') as f:
            raw_data = f.read()
            if raw_data:
                return json.loads(raw_data)

            return {}

    def put(self, key, value, timestamp):
        data = self.get_data()
        if key in data:
            data[key].append(([int(timestamp), float(value)]))
        else:
            data[key] = []
            data[key].append(([int(timestamp), float(value)]))

        with open(self.storage_path, 'w') as f:
            f.write(json.dumps(data))


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
