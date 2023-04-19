from Tile import * 
from Player import *
from Game_processor import *
from Deck import Deck
from Player import Player

from clueless.server.Game_message_handler import Game_message_handler
from clueless.server.Game_processor import Game_processor

class Game:

    def __init__(self, player_info_dict): # players, num_players):
        self.num_players = len(player_info_dict)
        self.players = []
        for player_id, player_name in player_info_dict.items():
            this_player = Player(player_name, player_id)
            self.players.append(this_player)
        
        deck = Deck()
        self.game_deck = deck.get_deck()                    # dict for initial overall game deck
        self.case_file = deck.get_secret_deck()             # dict of three secret cards
        # self.turn_state = None                             # turn state for current player
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

    # def get_turn_status(self):
    #     return self.turn_state

    def get_game_status(self):
        return self.game_status

    def get_case_file(self):
        return self.case_file

    def get_game_status(self):
        return self.game_status
    
    def get_game_board(self):
        return self.game_board

    # return a player whose turn it is not currently
    def get_player(self, player):
        if player in self.players:
            return self.get_player
        else:
            # unsure what we would want returned here, placeholder print
            print("That player is not in this game, please try again.")

    def get_player_object(self, player_id):
        for i, player in enumerate(self.players):
            if player.get_player_id() == player_id:
                return player
    
    # A method that deals a deck of cards to players 
    def deal_to_players(self)->dict:
        num_players= len(self.players)
        dealt_decks = Deck.deal(num_players)
        for i, player in enumerate(self.players):
            player.set_player_hand(dealt_decks[i])

    # Set case file for testing purposes
    def set_case_file(self, character, weapon, room):
        self.case_file = {character:'character',
                     weapon: 'weapon',
                     room:'room'}
    
    def set_case_file(self, character, weapon, room):
        self.case_file = {character:'character',
                     weapon: 'weapon',
                     room:'room'}
        
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
            {'player_id': str,
            'turn_status': str,                                 # movement, accusation, or suggestion
            'suggested_cards': dict,                            # client_message['suggested_cards']
            'accused_cards': dict,
            'target_tile': str
            } 
            
        OUTPUT: game_status : dictionary to be sent back to the Server containing information about the turn result
            {'player_token': str,
            'turn_status': str,                   # movement, accusation, or suggestion
            'suggested_cards': dict,
            'suggested_match_card' : str,
            'suggest_result_player': str,         # Name of player who provided suggested cards, None if no matching cards were found
            'accused_cards': dict,
            'accused_result_player' : str,        # Name of player who accused correctly, None accused incorrectly
            'target_tile': str
            } 
        '''
        # Get player object
        curr_player = self.get_player_object(player_turn['player_id'])
        
        #  Game status stores the result of player taking a turn
        game_status = player_turn.copy()
        
        # Execute specific turn and update corresponding game_status with result
        if player_turn['turn_status'] == "movement":  
            print(f"  Player {player_turn['player_id']} chooses to move to location {player_turn['target_tile']}")
            move_result_boolean = Game_processor.move(board_dict = self.game_board, player = curr_player, destination = player_turn['target_tile'])
            
        elif player_turn['turn_status'] == "accusation":
            print(f"  Player chooses to accuse {player_turn['accused_cards']['character']},{player_turn['accused_cards']['weapon']},{player_turn['accused_cards']['room']}")
            # TO DO: extract from player_turn
            accuse_result = Game_processor.accuse(player_turn['accused_cards']['character'], player_turn['accused_cards']['weapon'], player_turn['accused_cards']['room'], self.case_file)
            if accuse_result:
                print('    Player accused correctly')
                # Include name of current player if they accused correctly
                game_status['accused_result_player'] = curr_player.get_player_name()
            else: 
                curr_player.set_player_status('LOST')
            
        elif player_turn['turn_status'] == "suggestion":
            print('  Player chooses to suggest')
            # TO DO: extract from player_turn
            player_w_match, matched_card = Game_processor.suggest(curr_player.get_player_name(), player_turn['accused_cards']['weapon'], player_turn['accused_cards']['room'], player_turn['accused_cards']['character'])
            # TO DO: assumes output of suggest has name of player who suggested cards
            game_status['suggest_result_player'] = player_w_match
            game_status['suggested_match_card']= matched_card
            
        return game_status # --goes to--> server_update = Game_message_handler.build_game_package(game_status)
    
    
## ---------- MEGAN TESTING GROUNDS -----------
def pretty_print_dict(this_dict):
    for key in this_dict:
        print(f"  {key} : {this_dict[key]}")
        
# in Server.py
#   player_turn = Game_message_handler.process_client_update(client_message)
player_turn = {'player_id': '1',
            'turn_status': 'accusation',        # movement, accusation, or suggestion
            'suggested_cards': dict,            # client_message['suggested_cards']
            'accused_cards': {'character':'Mrs. White',
                              'weapon':'Rope',
                              'room':'Library'},
            'target_tile': ''
            } 
player_info_dict = {'1':'Colonel Mustard', 
                    '2':'Miss Scarlet'}
# Server initializes Game
game = Game(player_info_dict)
game.set_case_file(character='Mrs. White', weapon='Rope', room='Library')
case = game.get_case_file()
print('secret case file is ')
pretty_print_dict(case)
    
# --> in Game.py
print('Player taking a turn...')
game_status = game.player_take_turn(player_turn)
print()
print('Player finished turn... and resulting game_status is')
pretty_print_dict(game_status)