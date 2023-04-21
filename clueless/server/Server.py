#Server Module
import socket
import threading
import pickle
import sys
from clueless.server.Game import Game
from clueless.server.Game_message_handler import Game_message_handler
from clueless.server.Game_processor import *

HOST_ADDR = socket.gethostbyname(socket.gethostname())
HOST_PORT = 8080
DEFAULT_TURN = dict({'header': 'None', 'player_id': 'None', 'data': ''})
DEFAULT_GAME = dict({'player_count': 0, 'player_token': '0', 'turn_status': ''})
PLAYER_MAX = 6
PLAYER_MIN = 3
SKIP = 'skip'

class Server:

    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.id_count = 0
        self.max_players = PLAYER_MAX
        #hardcoding as a placeholder
        player_info_dict = {1:'Colonel Mustard',
                            2:'Miss Scarlet',
                            3:'Professor Plum'}
        self.game = Game(player_info_dict)
        self.clients = set()
        self.clients_lock = threading.Lock()

        try:
            self.server.bind((HOST_ADDR, HOST_PORT))
        except socket.error as err:
            str(err)

        print("Waiting for a connection, server started")
        self.start()

    def threaded_client(self, conn, player_id, game):
        conn.send(pickle.dumps(player_id))
        reply = ""
        prev_client_message = DEFAULT_TURN
        server_update = game
        connected = True

        while connected:
            try:
                #print("Server receiving player data")'
                client_message = Game_message_handler.receive_client_update(conn)
                #print("Server received player data")
    
                if not client_message:
                    print("Disconnected")
                    connected = False
                    break
                else:
                    if client_message != prev_client_message:
                        player_turn = Game_message_handler.process_client_update(client_message)
                        #print("processed client message")

                        if player_turn['turn_status'] != "get" and player_turn['turn_status'] != "MOVING" and player_turn['turn_status'] != "ACCUSING":
                            #print(player_turn)
                            # game_status = Game_processor.player_take_turn(player_turn)
                            game_status = self.game.player_take_turn(player_turn)
                            #print(game_status)
                            server_update = Game_message_handler.build_game_package(game_status)
                                                   
                        else:
                            server_update = player_turn
                        prev_client_message = client_message

                #print(server_update)
                with self.clients_lock:
                    for c in self.clients:
                        Game_message_handler.send_game_update(c, server_update)
                # Game_message_handler.send_game_update(conn, server_update)
                # print("... sent server update to client")
                # print()
            except:
                break

        print("Lost connection")
        try:
            print("Closing Game")
        except:
            pass

        conn.close()

        sys.exit("Server Closed")

    def start(self):
        id_count = self.id_count
        game_status = DEFAULT_GAME
        self.server.listen(2)

        #Enter the number of players and their names
        num_players= int(input("Enter the number of players: "))
        
        while (num_players < 3 or num_players > 6):
            print("A total number of 3-6 players are allowed to participate in this game.")
            num_players= int(input("Enter the number of players: "))

        self.max_players = num_players
                
        while True:
            self.id_count = id_count
        #this loops runs forever, so any print statements outside of 
        # the if statement will print forever

            if (id_count < PLAYER_MAX):
                conn, addr = self.server.accept()
                self.clients.add(conn)
                print("Connected to:", addr)
                game_status['player_count'] = id_count+1

                thread = threading.Thread(target=self.threaded_client, args=(conn, id_count+1, game_status))
                thread.start()
                id_count = threading.active_count()-1
                print("Active Players: ", threading.active_count()-1)
                print()

