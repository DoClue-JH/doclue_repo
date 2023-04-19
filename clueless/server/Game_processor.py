import random

class Game_processor:
    WEAPONS = ['candlestick','dagger','leadpipe','revolver','rope','wrench']
    TOKENS = ['Professor Plum','Mrs Peacock','Mr Green','Mrs White','Miss Scarlet','Colonel Mustard']
    ROOMS = ['Study','Library','Lounge', 'Billiard Room', 'Dining Room', 'Conservatory', 'Ballroom', 'Kitchen']

    def __init__(self, players, weapons, rooms, solution):
        self.players = players
        self.weapons = weapons
        self.rooms = rooms
        self.solution = solution
        self.cards = players + weapons + rooms
        self.deck = self.cards.copy()
        random.shuffle(self.deck)
        self.player_positions = {player: None for player in players}
        self.suggestions = []
        self.accusations = []
        self.player_cards = {player: [] for player in players}
        self.game_over = False

    def __init__(self) -> None:
        pass


#      # This method deals out the cards in the deck to each player. It does not
#      # return anything, but it modifies the player_cards and deck attributes 
#      # of the ClueGame object.   
#     def deal_cards(self):
#         for i, card in enumerate(self.deck):
#             self.player_cards[self.players[i % len(self.players)]].append(card)
#         self.deck = []

    

    # prompt still needs to be moved to FRONT END
    def prompt_move(player):
        print()
        print("===============================")
        print("       **Movement Phase**      ")
        print("      **", player.player_name, "**")
        print("===============================")
        print()
        print("Instructions:")
        print("Please enter a valid tile name from above, without apostrophes.")

        player_input_tile = input("Where do you want to go? \n")
        return player_input_tile

    # split into server-side retrieve and client-display valid moves
    def show_valid_moves(player, board_dict):

        if (player.get_player_old_location() is None) and (player.get_player_current_location() is None):

            player_first_move = {
            'Miss Scarlet' : 'Hallway 02',
            'Professor Plum' : 'Hallway 03',
            'Colonal Mustard' : 'Hallway 05',
            'Mrs. Peacock' : 'Hallway 08',
            'Mr. Green' : 'Hallway 11',
            'Mrs. White' : 'Hallway 12'
            }

            
            print()
            print("####################################################################")
            print("Looks like this is your first move! You have to move to your starting")
            print("tile, but don't worry, you'll get to pick where you go next time.")
            print()
            print("**********************************")
            print("Your starting tile is:", player_first_move.get(player.get_player_name()))
            print("**********************************")
            return

        print(player.get_player_name(), "is in", player.get_player_current_location())

        # create list of ALL adjacent tiles
        # create empty list for valid tiles player can move to after they've been checked for validity
        print(player.get_player_current_location())
        temp_adjacent_tiles = board_dict.get(player.get_player_current_location()).get_adjacent_tiles()
        temp_valid_tiles = []

        print("Tiles adjacent to", player.get_player_current_location(), "are",  temp_adjacent_tiles)

        # iterate over all tiles in the adjacent list
        for tile in temp_adjacent_tiles:
            # if NO ONE is on the tile, then automatically valid move (adj and empty); append to valid tiles
            #   else if the tile type is ROOM and there are 1 or more players on it, this is also valid, append
            # all other cases are INVALID (1 player and HALLWAY is invalid, hallway is considered full)
            if board_dict.get(tile).get_tile_num_players() == 0:
                temp_valid_tiles.append(tile)
            elif board_dict.get(tile).get_tile_num_players() >= 1 and board_dict.get(tile).get_tile_type() == "room":
                temp_valid_tiles.append(tile)
        print()
        print("####################################################################")
        print("Tiles that are valid moves are:", temp_valid_tiles)
        print("####################################################################")
        return 

    def move(self, board_dict, player, destination):
        # validate gets called first
        if self.validate_move(board_dict, player, destination) == True:
            # update player old and new location
            player.update(destination)
            print("old is", player.get_player_old_location())
            print("new is", player.get_player_current_location())

            # update tile_num_players
            if player.get_player_old_location() is not None:
                board_dict.get(player.get_player_old_location()).tile_num_players -= 1

            board_dict.get(player.get_player_current_location()).tile_num_players += 1

            # print statements
            print()
            print("Success!")
            print("Previous tile:", player.get_player_old_location())
            if player.get_player_old_location() is not None:
                print(player.get_player_old_location(), "now has", board_dict.get(player.get_player_old_location()).get_tile_num_players(), "players on it.")
            print(player.get_player_current_location(), "now has", board_dict.get(player.get_player_current_location()).get_tile_num_players(), "players on it.")
            print()
            print(player.get_player_name(), "has moved to", board_dict.get(player.get_player_current_location()).tile_name)
            print()
            print("===============================")
            return True
        
        elif self.validate_move(board_dict, player, destination) == False:
            return False


    # check if move is in dict; if in dict, is it in the adj tiles?
    def validate_move(board_dict, player, destination):

        # check if this is the player's first move, the only time where
        # both old and new location are None
        if (player.get_player_old_location() is None) and (player.get_player_current_location() is None):

            # dict of player_name : starting tile_name
            player_first_move = {
                'Miss Scarlet' : 'Hallway 02',
                'Professor Plum' : 'Hallway 03',
                'Colonal Mustard' : 'Hallway 05',
                'Mrs. Peacock' : 'Hallway 08',
                'Mr. Green' : 'Hallway 11',
                'Mrs. White' : 'Hallway 12'
                }
            
            if player_first_move.get(player.player_name) == destination:
                return True
            else:
                return False
        

        # create list of ALL adjacent tiles
        # create empty list for valid tiles player can move to after they've been checked for validity
        # print(player.get_player_current_location())
        temp_adjacent_tiles = board_dict.get(player.get_player_current_location()).get_adjacent_tiles()
        temp_valid_tiles = []

        # print("Tiles adjacent to", player.get_player_current_location(), "are",  temp_adjacent_tiles)

        # iterate over all tiles in the adjacent list
        for tile in temp_adjacent_tiles:
            # if NO ONE is on the tile, then automatically valid move (adj and empty); append to valid tiles
            #   else if the tile type is ROOM and there are 1 or more players on it, this is also valid, append
            # all other cases are INVALID (1 player and HALLWAY is invalid, hallway is considered full)
            if board_dict.get(tile).get_tile_num_players() == 0:
                temp_valid_tiles.append(tile)
            elif board_dict.get(tile).get_tile_num_players() >= 1 and board_dict.get(tile).get_tile_type() == "room":
                temp_valid_tiles.append(tile)


        # check if the tile player wants to move to is in the list of remaining valid move options
        if destination in temp_valid_tiles:
            return True
        else: 
            return False

    # This method determines what turn the player is taking and then routes to 
    # appropriate game logic functions to carry out turn accordingly
    def player_take_turn(player_turn):
        print("Player taking turn: Player ", player_turn['player_id'])

        if player_turn['turn_status'] == "movement":
            print("Player chooses to move to location ", player_turn['target_tile'])
            print()
            
        return player_turn

    # This method records an accusation made by a player. It does not return
    # anything, but it modifies the accusations attribute of the ClueGame object. 
    # If the accusation is correct
    def accuse(player, weapon, room, case_file):
        case_file_reversed = {card_type: card_val for card_val, card_type in case_file.items()}
        
        # If accusation is correct, return True
        return player == case_file_reversed['character'] and weapon == case_file_reversed['weapon'] and room == case_file_reversed['room']   

        
        
        
    #     # This method returns the list of accusations made by a specific player.
    #     def get_accusations_for_player(self, player):
    #         player_accusations = []
    #         for accusation in self.accusations:
    #             if accusation['player'] == player:
    #                 player_accusations.append(accusation)
    #         return player_accusations

    #     # This method returns the list of cards held by a specific player.   
    #     def get_player_cards(self, player):
    #         return self.player_cards[player]

    # # create a new game
    # game = Game_processor()

    # # make a suggestion by player 1
    # game.suggestion("player1", "wrench", "study", "player2")

    # # validate the suggestion
    # is_valid = game.validate_suggestion(("player1", "wrench", "study", "player2"))
    # if is_valid:
    #     print("Valid suggestion!")
    # else:
    #     print("Invalid suggestion.")