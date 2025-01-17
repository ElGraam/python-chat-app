import socket

from protocol.super_protocol import BaseSocket


class TCPClient:
    def __init__(self):
        self.server_address = None
        self.server_port = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.base_socket = BaseSocket()

    def connect(self):
        try:
            self.socket.connect((self.server_address, self.server_port))
            print(
                "Connected to the server at {}:{}".format(
                    self.server_address, self.server_port
                )
            )
        except socket.error as e:
            print(f"Error connecting to server: {e}")
            return False  # 返り値で接続の成否を示す
        return True

    def receive_message(self):
        try:
            response_bytes = self.socket.recv(self.base_socket.buffer)

            if not response_bytes:
                print("No data received.")
                return None  # 接続が閉じられたか、データが空であることを示す

            if len(response_bytes) != 707:  # header+bodyは32bytesであることを期待
                print("Received incomplete data.")
                return None

            message_dict = self.base_socket.header_and_body_to_dict(response_bytes)
            return message_dict

        except socket.error as e:
            print(f"Error receiving data: {e}")
            self.close_connection()
            return None

    def send_request(self, parameter: dict):
        self.base_socket.dict_to_bytes(parameter)
        try:
            if self.socket.fileno() == -1:
                print("Socket is already closed.")
                return False
            self.socket.sendall(self.base_socket.header + self.base_socket.body)
        except socket.error as e:
            print(f"Error sending data: {e}")
            self.close_connection()
            return False
