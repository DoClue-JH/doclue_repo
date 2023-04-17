from Tile import * 
from Player import *
from Game_processor import *
from Deck import Deck
from Player import Player

from clueless.server.Game_message_handler import Game_message_handler
from clueless.server.Game_processor import Game_processor

class Game:

    def __init__(self, players, num_players):
        self.num_players = num_players
        self.players = players                              # list of all players
        self.game_deck = Deck.get_deck()                    # dict for initial overall game deck
        self.case_file = Deck.get_secret_deck()             # dict of three secret cards
        # self.turn_state = None                              # turn state for current player
        self.game_status = None                             # game state of entire game

        ############################
        ##### INITIALIZE TILES #####
        # to initialize an object of class tile
        # self, tile_name, tile_type, adjacent_tiles
        ############################
        #
        # INITIALIZE ROOM TILES
        # with their str name, "room", and adj tiles
        tile_study = Tile("Study", "room", ["Hallway 01", "Hallway 03", "Kitchen"])
        tile_hall = Tile("Hall", "room", ["Hallway 01", "Hallway 02"])
        tile_lounge = Tile("Lounge", "room", ["Hallway 02", "Hallway 05", "Conservatory"])
        tile_library = Tile("Library", "room", ["Hallway 03", "Hallway 06", "Hallway 08"])
        tile_billiard_room = Tile("Billiard Room", "room", ["Hallway 06", "Hallway 04", "Hallway 09", "Hallway 07"])
        tile_dining_room = Tile("Dining Room", "room", ["Hallway 05", "Hallway 07", "Hallway 10"])
        tile_conservatory = Tile("Conservatory", "room", ["Hallway 08", "Hallway 11", "Lounge"])
        tile_ballroom = Tile("Ballroom", "room", ["Hallway 11", "Hallway 09", "Hallway 12"])
        tile_kitchen = Tile("Kitchen", "room", ["Hallway 12", "Hallway 10", "Study"])

        # INITIALIZE HALLWAY TILES
        # with their str name, "hallway", and adj tiles
        tile_hallway_01 = Tile("Hallway 01", "hallway", ["Study", "Hall"])
        tile_hallway_02 = Tile("Hallway 02", "hallway", ["Hall", "Lounge"])
        tile_hallway_03 = Tile("Hallway 03", "hallway", ["Study", "Library"])
        tile_hallway_04 = Tile("Hallway 04", "hallway", ["Hall", "Billiard Room"])
        tile_hallway_05 = Tile("Hallway 05", "hallway", ["Lounge", "Dining Room"])
        tile_hallway_06 = Tile("Hallway 06", "hallway", ["Library", "Billiard Room"])
        tile_hallway_07 = Tile("Hallway 07", "hallway", ["Billiard Room", "Dining Room"])
        tile_hallway_08 = Tile("Hallway 08", "hallway", ["Library", "Conservatory"])
        tile_hallway_09 = Tile("Hallway 09", "hallway", ["Billiard Room", "Dining Room"])
        tile_hallway_10 = Tile("Hallway 10", "hallway", ["Dining Room", "Kitchen"])
        tile_hallway_11 = Tile("Hallway 11", "hallway", ["Conservatory", "Ballroom"])
        tile_hallway_12 = Tile("Hallway 12", "hallway", ["Ballroom", "Kitchen"])

        ##### END TILES #####

        ############################
        ##### BOARD DICTIONARY #####
        ############################
        # initialize dictionary of tile_name to tile object
        # referred to as board_dict generally

        self.game_board = {
            # ROOMS
            'Study': tile_study,
            'Hall': tile_hall,
            'Lounge': tile_lounge,
            'Library': tile_library,
            'Billiard Room': tile_billiard_room,
            'Dining Room': tile_dining_room,
            'Conservatory': tile_conservatory,
            'Ballroom': tile_ballroom,
            'Kitchen': tile_kitchen,
            # HALLWAYS
            'Hallway 01' : tile_hallway_01,
            'Hallway 02' : tile_hallway_02,
            'Hallway 03' : tile_hallway_03,
            'Hallway 04' : tile_hallway_04,
            'Hallway 05' : tile_hallway_05,
            'Hallway 06' : tile_hallway_06,
            'Hallway 07' : tile_hallway_07,
            'Hallway 08' : tile_hallway_08,
            'Hallway 09' : tile_hallway_09,
            'Hallway 10' : tile_hallway_10,
            'Hallway 11' : tile_hallway_11,
            'Hallway 12' : tile_hallway_12
            }
        
        # Find out where Game is initialized, loop through players and map their name to id
        # self.player_name_to_connectionid_dict = 

    def get_turn_status(self):
        return self.turn_state

    def get_game_status(self):
        return self.game_status

    def get_case_file(self):
        return self.case_file

    def get_current_player(self):
        return self.get_turn_status

    def get_game_status(self):
        return self.get_turn_status

    def get_case_file(self):
        return self.get_case_file
    
    def get_game_board(self):
        return self.game_board


    # return a player whose turn it is not currently
    def get_player(self, player):
        if player in self.players:
            return self.get_player
        else:
            # unsure what we would want returned here, placeholder print
            print("That player is not in this game, please try again.")

    def get_player(self, player_id):
        for i, player in enumerate(self.players):
            if player.get_player_id() == player_id:
                return player
    
    # A method that deals a deck of cards to players 
    def deal_to_players(self)->dict:
        num_players= len(self.players)
        dealt_decks = Deck.deal(num_players)
        for i, player in enumerate(self.players):
            player.set_player_hand(dealt_decks[i])


# Khue Test Statements for Move
# show valid moves, prompt, take input is the loop
# test statement

# miss_scarlet = Player("Miss Scarlet", 1)
# players = []
# players.append(miss_scarlet)

# game = Game(players, len(players))

# # movement phase for one player
# while True:
#     show_valid_moves(miss_scarlet, game.get_game_board())
#     move_input = prompt_move(miss_scarlet)
#     move_output = move(game.game_board, miss_scarlet, move_input)

#     if move_output == True:
#         break       # continue to next phase

#     else:
#         print("Invalid move, try again!")

# while True:
#     show_valid_moves(miss_scarlet, game.get_game_board())
#     move_input = prompt_move(miss_scarlet)
#     move_output = move(game.game_board, miss_scarlet, move_input)

#     if move_output == True:
#         break       # continue to next phase

#     else:
#         print("Invalid move, try again!")




# Khue Test Statements for Move
# show valid moves, prompt, take input is the loop
# test statement

# miss_scarlet = Player("Miss Scarlet", 1)
# players = []
# players.append(miss_scarlet)

# game = Game(players, len(players))

# # movement phase for one player
# while True:
#     show_valid_moves(miss_scarlet, game.get_game_board())
#     move_input = prompt_move(miss_scarlet)
#     move_output = move(game.game_board, miss_scarlet, move_input)

#     if move_output == True:
#         break       # continue to next phase

#     else:
#         print("Invalid move, try again!")

# while True:
#     show_valid_moves(miss_scarlet, game.get_game_board())
#     move_input = prompt_move(miss_scarlet)
#     move_output = move(game.game_board, miss_scarlet, move_input)

#     if move_output == True:
#         break       # continue to next phase

#     else:
#         print("Invalid move, try again!")



    # This method determines what turn the player is taking and then routes to 
    # appropriate game logic functions to carry out turn accordingly
    def player_take_turn(self, player_turn):
        '''
        INPUT: player_turn : dictionary from Game_message_handler.process_client_update(client_message)
            {'turn_status': player_status or'skip', 
            'player_token' : player_id, 
            'player_details' : desired location?
            }
        OUTPUT: game_status : dictionary to be sent back to the Server containing information about the turn result
            {'player_token':'',
            'turn_status':'', # Movement, Accusation, or Suggestion
            'suggested_cards':'',  # dict
            'suggest_result_player':'', # Name of player who provided suggested cards, None if no matching cards were found
            'accused_cards':'', # dict
            'target_tile':'' # string
            } 
        '''
        # Get player object
        curr_player = self.get_player(player_turn['player_token'])
        
        # Build game status from the result of player taking a turn
        game_status = {'player_token':'',
                       'turn_status':'', # Movement, Accusation, or Suggestion
                       'suggested_cards':'',  # dict
                       'suggest_result_player':'', # Name of player who provided suggested cards, None if no matching cards were found
                       'accused_cards':'', # dict
                       'target_tile':'' # string
                       } 
        
        if player_turn['player_status'] == "MOVING": #"CHOOSING":
            destination = player_turn['player_details']
            print("Player taking turn: Player ", player_turn['player_id'])
            print("Player chooses to move to location ", player_turn['player_details'], end='\n')
            # move_result = Game_processor.move(player, destination)
            
        elif player_turn['player_status'] == "ACCUSING":
            print('Player chooses to accuse')
            accuse_result = Game_processor.accuse(player, weapon, room)
            if accuse_result: 
                curr_player.set_player_status('LOST')
            
        elif player_turn['player_status'] == "SUGGESTING":
            print('Player chooses to suggest')
            # suggest_result = Game_processor.suggest(player, weapon, room, accused_player)
            
        return game_status # --> server_update = Game_message_handler.build_game_package(game_status)
    
    
    
    
# ---------- MEGAN TESTING GROUNDS ----------
# ---------- within Game class ----------
# (1) assume this is done
#   Game_message_handler.test_process_sent_package() --> 
package_data = {'current_player':'megan', 
                'character':'mrs white',
                'weapon':'rope',
                'room':'study'}

# (2) call accuse in game_processor feeding in package info
#   returns True or False
accuse_result = Game_processor.accuse(package_data['player'], package_data['weapon'], package_data['room'])
# Build contents by adding accuse_result
contents = package_data.copy()
contents['accuse_result'] = accuse_result
# (3) TO IMPLEMENT build server_status by Game_message_handler.test_build_return_package(state, contents): 
'''
    player_tokens : list
    player_status :  (player who just finished a turn?)
    turn_status : TURN_STATUS
        Movement
        Accusation  
        Suggestion
    suggest_result : string
        Non-empty, card value of match if match
    accuse_result : string
        Non-empty, “correct” if match
    accuse_info : dict 
        Non-empty, [‘player_name’+accused_deck]
    if_placed: bool
        If player token was moved on a previous turn
    player_location: string
        Name of tile where the player is located
'''
# ---------- inside Game class or inside Game_message_handler? ----------
server_status = {'player_tokens':[], # all player tokens, self.players from Game
                 'player_status':'',
                 'turn_status':'Accusation',
                 'suggest_result':'',
                 'accuse_result':'',
                 'accuse_info':[package_data['current_player'], package_data['player'], package_data['weapon'], package_data['room']],
                 'if_placed':'',
                 'player_location':''}
if accuse_result:
    server_status['accuse_result'] = 'CORRECT' 
else:
    server_status['accuse_result'] = 'INCORRECT' 
    server_status['player_status'] = 'LOST' 
    
# (4) TO IMPLEMENT send server_status by Game_message_handler.send_game_update()
# Game_message_handler.test_send_game_update(server_status)



# ---------- outside Game class ----------
# (5) TO TEST Client_message_handler.receive()