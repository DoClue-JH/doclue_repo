from Deck import Deck
from Player import Player

class Game:

    def __init__(self, num_players, players, game_board, player_id, turn_state, game_status): # I took these attributes (game_deck, case_file) out
        self.num_players = num_players
        self.players = []
        for player_name in players:
            this_player = Player(player_name,player_id)   
            self.players.append(this_player) 
        self.game_board = game_board
        deck= Deck()
        self.game_deck = deck.get_deck()
        self.case_file = deck.get_secret_deck()
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
    
    # A method that deals a deck of cards to players 
    def deal_to_players(self)->dict:
        num_players= len(self.players)
        dealt_decks = Deck.deal(num_players)
        for i, player in enumerate(self.players):
            player.set_player_hand(dealt_decks[i])
