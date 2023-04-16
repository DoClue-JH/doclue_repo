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


    # This method determines what turn the player is taking and then routes to 
    # appropriate game logic functions to carry out turn accordingly
    def player_take_turn(player_turn):
        if player_turn['player_status'] == "CHOOSING":
            print("Player taking turn: Player ", player_turn['player_id'])
            print("Player chooses to move to location ", player_turn['player_details'])
            print()
        return player_turn


#      # This method deals out the cards in the deck to each player. It does not
#      # return anything, but it modifies the player_cards and deck attributes 
#      # of the ClueGame object.   
#     def deal_cards(self):
#         for i, card in enumerate(self.deck):
#             self.player_cards[self.players[i % len(self.players)]].append(card)
#         self.deck = []

#     # This method moves a player to a new position. It does not return anything,
#     # but it modifies the player_positions attribute of the ClueGame object.    
#     def move(self, player, destination):
#         '''
#         Move a player to a new position.
#         If the move is valid, update the player's position and print the new position.
#         If the move is not valid, print a message indicating that the move is not allowed.
#         '''
#         if self.validate_move(player, destination):
#             self.player_positions[player] = destination
#             print(f"{player} moved to {destination}.")
#         else:
#             print(f"Invalid move for {player}. Cannot move to {destination}.")

#     # This method checks if a move is valid for a player. It returns a Boolean
#     # value indicating whether or not the move is valid.        
#     def validate_move(self, player, destination):
#         if destination not in self.rooms and destination not in self.player_positions.values():
#             return True
#         return False
#     # This method returns the list of valid moves a player can make based on 
#     # their current position.
#     def get_valid_moves(self, player):
#         valid_moves = []
#         for room in self.rooms:
#             if room not in self.player_positions.values():
#                 valid_moves.append(room)
#         if self.player_positions[player] in self.rooms:
#             valid_moves.append(self.player_positions[player])
#         return valid_moves

#     # This method records a suggestion made by a player. It does not return 
#     # anything, but it modifies the suggestions attribute of the ClueGame object.    
#     def suggestion(self, player, weapon, room, accused_player):
#         suggestion = {'player': player, 'weapon': weapon, 'room': room, 'accused_player': accused_player}
#         self.suggestions.append(suggestion)

#     # This method checks if a suggestion is valid. It returns a Boolean value 
#     # indicating whether or not the suggestion is valid.    
#     def validate_suggestion(self, suggestion):
#         if suggestion['player'] not in self.players or suggestion['weapon'] not in self.weapons or suggestion['room'] not in self.rooms or suggestion['accused_player'] not in self.players:
#             return False
#         return True
    
#     # This method returns the list of suggestions made by a specific player.
#     def get_suggestions_for_player(self, player):
#         player_suggestions = []
#         for suggestion in self.suggestions:
#             if suggestion['player'] == player:
#                 player_suggestions.append(suggestion)
#         return player_suggestions
    
    # This method records an accusation made by a player. It does not return
    # anything, but it modifies the accusations attribute of the ClueGame object. 
    # If the accusation is correct, it also sets the game_over attribute to True.  
    def accuse(self, player, weapon, room):
        accusation = {'player': player, 'weapon': weapon, 'room': room}
        self.accusations.append(accusation) # QUESTION: What's the purpose of appending accusations?
        # If accusation is correct
        if player == self.solution['player'] and weapon == self.solution['weapon'] and room == self.solution['room']:
            self.game_over = True
            # return winner name
            return True
        # If accusation is incorrect
        else: 
            # TO DO 
            # set player to lost/inactive
            # only display lost and case file to losing player
            # continue to next turn
            return False
        # TO DO 
        #   update game_status?
        #   send game_status to Game_message_handler
        #   Game_message_handler receive_game_status()
        #   Game_message_handler build_return_package()
        #   someone send package to Client_message_handler

    # This method checks if an accusation is valid. It returns a Boolean value 
    # indicating whether or not the accusation is valid.   
    def validate_accusation(self, accusation):
        '''
        INPUT: accusation : list of three user inputs
        OUTPUT: True if accusation is valid, False otherwise
        '''
        # Precondition: accusation is cleaned up syntax to match my lists of weapons, tokens, and rooms
        has_weapon = False
        has_token = False
        has_room = False
        for guess in accusation:
            if guess in self.WEAPONS: has_weapon = True
            elif guess in self.TOKENS: has_token = True
            elif guess in self.ROOMS: has_room = True
        return has_weapon and has_token and has_room
    
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
