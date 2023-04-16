from Tile import * 
from Player import *
from Game_processor import *

class Game:

    def __init__(self, num_players, players, game_board, game_deck, case_file, turn_state, game_status):
        self.num_players = num_players
        self.players = players
        self.game_board = game_board
        self.game_deck = game_deck
        self.case_file = case_file
        self.turn_state = turn_state
        self.game_status = game_status
        
        # Find out where Game is initialized, loop through players and map their name to id
        # self.player_name_to_connectionid_dict = 

    def get_turn_status():
        pass

    def get_current_player():
        pass

    def get_game_status():
        pass

    def get_case_file():
        pass

    def get_player():
        pass

############################
##### INITIALIZE TILES #####
# to initialize an object of class tile
# self, tile_name, tile_type, adjacent_tiles
############################
#
# INITIALIZE ROOM TILES
# with their str name, "ROOM", 0 players on tile, not occupied, and adj tiles
tile_study = Tile("Study", "ROOM", ["hw_01", "hw_03", "Kitchen"])
tile_hall = Tile("Hall", "ROOM", ["hw_01", "hw_02"])
tile_lounge = Tile("Lounge", "ROOM", ["hw_02", "hw_05", "Conservatory"])
tile_library = Tile("Library", "ROOM", ["hw_03", "hw_06", "hw_08"])
tile_billiard_room = Tile("Billiard Room", "ROOM", ["hw_06", "hw_04", "hw_09", "hw_07"])
tile_dining_room = Tile("Dining Room", "ROOM", ["hw_05", "hw_07", "hw_10"])
tile_conservatory = Tile("Conservatory", "ROOM", ["hw_08", "hw_11", "Lounge"])
tile_ballroom = Tile("Ballroom", "ROOM", ["hw_11", "hw_09", "hw_12"])
tile_kitchen = Tile("Kitchen", "ROOM", ["hw_12", "hw_10", "Study"])

# INITIALIZE HALLWAY TILES
# with their str name, "HALLWAY", 0 players on tile, not occupied, and adj tiles
tile_hw_01 = Tile("hw_01", "HALLWAY", ["Study", "Hall"])
tile_hw_02 = Tile("hw_02", "HALLWAY", ["Hall", "Lounge"])
tile_hw_03 = Tile("hw_03", "HALLWAY", ["Study", "Library"])
tile_hw_04 = Tile("hw_04", "HALLWAY", ["Hall", "Billiard Room"])
tile_hw_05 = Tile("hw_05", "HALLWAY", ["Lounge", "Dining Room"])
tile_hw_06 = Tile("hw_06", "HALLWAY", ["Library", "Billiard Room"])
tile_hw_07 = Tile("hw_07", "HALLWAY", ["Billiard Room", "Dining Room"])
tile_hw_08 = Tile("hw_08", "HALLWAY", ["Library", "Conservatory"])
tile_hw_09 = Tile("hw_09", "HALLWAY", ["Billiard Room", "Dining Room"])
tile_hw_10 = Tile("hw_10", "HALLWAY", ["Dining Room", "Kitchen"])
tile_hw_11 = Tile("hw_11", "HALLWAY", ["Conservatory", "Ballroom"])
tile_hw_12 = Tile("hw_12", "HALLWAY", ["Ballroom", "Kitchen"])

##### END TILES #####

############################
##### BOARD DICTIONARY #####
############################
# initialize dictionary of tile_name to tile object
# referred to as board_dict generally

board_tiles = {
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
    'hw_01' : tile_hw_01,
    'hw_02' : tile_hw_02,
    'hw_03' : tile_hw_03,
    'hw_04' : tile_hw_04,
    'hw_05' : tile_hw_05,
    'hw_06' : tile_hw_06,
    'hw_07' : tile_hw_07,
    'hw_08' : tile_hw_08,
    'hw_09' : tile_hw_09,
    'hw_10' : tile_hw_10,
    'hw_11' : tile_hw_11,
    'hw_12' : tile_hw_12
    }

def prompt_move(player):
    print()
    print("===============================")
    print("       **Movement Phase**      ")
    print("      **", player.player_name, "**")
    print("===============================")
    print()
    print("Instructions:")
    print("If this is your first turn, go ahead and enter whatever you want;")
    print("your character has a predetermined first move. Otherwise, please")
    print("type in a room from the list of rooms given to you without the ")
    print("apostrophes. Please note that the names are case-sensitive!")
    print()

    player_input_tile = input("Where do you want to go? \n")
    return player_input_tile

# ms_scarlet = Player("Ms. Scarlet", 1, None)
# input_string = prompt_move(ms_scarlet)
# move(board_tiles, ms_scarlet, input_string)

# input_string = prompt_move(ms_scarlet)
# move(board_tiles, ms_scarlet, input_string)

#move(board_tiles, ms_scarlet, "Hall")
#move(board_tiles, ms_scarlet, "Study")