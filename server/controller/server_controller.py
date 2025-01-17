import threading

from server.models.server_model import ServerModel


class ServerController:

    def __init__(self):
        self.server_model = ServerModel()

    def server_tcp_create_handler(self, client_connection):
        # 部屋の作成か、部屋の参加をする用の関数
        self.server_model.create_or_join_server_room_prompt(client_connection)

    def server_tcp_handler(self):
        # TCPで接続してきたクライアントを制御するための関数
        while True:
            connection, address = self.server_model.tcp_accept()
            client_handler = threading.Thread(
                target=self.server_tcp_create_handler, args=(connection,)
            )
            client_handler.start()

    def server_udp_handler(self):
        # UDPを利用して、メッセージを送信するための関数
        self.server_model.start_udp_server()

    def start(self):
        # 接続のセットアップ
        self.server_model.setup()
        print("-- server start --")

        # TCP
        client_tcp_handler = threading.Thread(target=self.server_tcp_handler, args=())

        # UDP
        client_udp_handler = threading.Thread(target=self.server_udp_handler, args=())
        client_udp_handler.start()
        client_tcp_handler.start()
