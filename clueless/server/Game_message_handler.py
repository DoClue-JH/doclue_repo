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
    
    # what would state be? do we need it?
    def test_build_return_package(self, state, contents):         
        # status = state
        # package = dict({'header': status, 'player_id': self.id, 'data': contents})
        server_status = {'player_tokens':[], # all player tokens, self.players from Game
                 'player_status':'',
                 'turn_status':'Accusation',
                 'suggest_result':'',
                 'accuse_result':'',
                 'accuse_info':[contents['current_player'], contents['player'], contents['weapon'], contents['room']],
                 'if_placed':'',
                 'player_location':''}
        # Build package for accusation result if state is accusation
        if state == 'ACCUSATION':
            accuse_result = contents['accuse_result']
            if accuse_result:
                server_status['accuse_result'] = 'CORRECT' 
            else:
                server_status['accuse_result'] = 'INCORRECT' 
                server_status['player_status'] = 'LOST' 
        return server_status