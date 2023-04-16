from clueless.server.Game_message_handler import Game_message_handler
from clueless.server.Game_processor import Game_processor

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