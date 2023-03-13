# #Multi-Client Network Module
import socket
import pickle

HOST_ADDR = "192.168.1.24"
HOST_PORT = 8080

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = HOST_ADDR
        self.port = HOST_PORT
        self.addr = (self.server, self.port)
        self.player = self.connect()

    def get_player(self):
        return self.player

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048*2))
        except socket.error as err:
            print(err)