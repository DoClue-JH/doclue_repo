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

