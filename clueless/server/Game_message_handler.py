import socket
import pickle
import threading

class Game_message_handler:

    def __init__(self):
        pass

    def send_game_update():
        pass

    def receive_game_status():
        pass

    def process_sent_package():
        pass

    def build_return_package():
        pass
    
    
## MEGAN TESTING GROUNDS
    def test_process_sent_package(self):
        try:
            return pickle.loads(self.client.recv(4096))
        except socket.error as err:
            print(err)

    def test_send_game_update(self, data):
        print("Server sending information to clients")
        try:
            self.client.send(pickle.dumps(data)) # client to be changed to server
        except socket.error as err:
            print(err)