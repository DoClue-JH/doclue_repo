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

        #self.game = Game(player_info_dict, 3)

        #self.game = Game([],3)

        try:
            self.server.bind((HOST_ADDR, HOST_PORT))
        except socket.error as err:
            str(err)

        print("Waiting for a connection, server started")
        print()
        self.start()

    def threaded_client(self, conn, player_id, game_status):
        conn.send(pickle.dumps(player_id))
        reply = ""
        prev_client_message = DEFAULT_TURN
        server_update = game_status
        connected = True

        while connected:
            try:
                #print("Server receiving player data")
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
                        #print("processed client message")

                        if player_turn['turn_status'] != "get" and player_turn['turn_status'] != "MOVING" and player_turn['turn_status'] != "ACCUSING":

                            if player_turn['turn_status'] == "join":
                                # add new player to the game
                                self.game.add_player(player_turn['player_id'], player_turn['player_token'])
                                player = self.game.get_player_object(player_turn['player_id'])
                                print("Added new player to the game: Player "+ player.get_player_id() + " is playing " + player.get_player_name())
                                print()

                                player_turn['turn_status'] = "get"

                                if (self.id_count == self.max_players and not self.game.dealt):
                                    print("All players have joined the game")
                                    print("dealing cards to players")
                                    print()
                                    self.game.deal_to_players()
                                    self.game.dealt = True
                                    self.game.set_turn_order()
                                    print("Let's start the game!")
                                    print()
                                    player_turn['turn_status'] = "start game"
                                    player_turn['next_player_turn'] = self.game.get_first_player()

                                server_update = Game_message_handler.build_game_package(player_turn)

                            elif player_turn['turn_status'] != "get":
                                game_status = self.game.player_take_turn(player_turn)
                                #print(game_status)
                                server_update = Game_message_handler.build_game_package(game_status)
                            else:
                                server_update = player_turn

                        prev_client_message = client_message
                        # #print(server_update)
                        # with self.clients_lock:
                        #     for c in self.clients:
                        #         Game_message_handler.send_game_update(c, server_update)
                        #         # if server_update['turn_status']!='get':
                        #             # print(f'client {c} received {server_update}')
                # print()
                # Game_message_handler.send_game_update(conn, server_update)
                try:
                    Game_message_handler.broadcast(self.clients, server_update)
                except Exception as err:
                    # index = self.clients.index(conn)
                    # self.clients.remove(conn)
                    # conn.close()
                    print(err)
                    break
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

        print("Welcome to Clueless!")
        #Enter the number of players and their names
        num_players= int(input("Please enter the number of players: "))
        
        while (num_players < PLAYER_MIN or num_players > PLAYER_MAX):
            print("A total number of 3-6 players are allowed to participate in this game.")
            num_players= int(input("Enter the number of players: "))

        self.max_players = num_players

        print("Game is loading...")
        self.game = Game(num_players)
        print("Waiting for players to join...")

        #this is the while loop that will continue to run indefinietly for the server
        while True:
            self.id_count = id_count


            if (id_count < PLAYER_MAX):
                #socket function called, waiting for an incoming connection from a new client
                conn, addr = self.server.accept()
                print("Connected to:", addr)
                
                game_status['player_count'] = id_count+1

                #open new thread for new client server connection to run on
                thread = threading.Thread(target=self.threaded_client, args=(conn, id_count+1, game_status))
                thread.start()
                id_count = threading.active_count()-1
                print("Active Players: ", threading.active_count()-1)
                print(id_count)
                print("Waiting for all players to join...")
                print()

