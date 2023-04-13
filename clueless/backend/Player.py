class Player:
    
    def __init__(self, player_name, player_id, player_current_location, player_old_location, player_hand, turn_status, player_status, player_notebook):
        self.player_name = player_name                          # string
        self.player_id = player_id                              # int
        self.player_current_location = player_current_location  # Tile
        self.player_old_location = player_old_location          # Tile
        self.player_hand = player_hand                          # Deck
        self.turn_status = turn_status                          # Enum (int)
        self.player_status = player_status                      # Enum (int)
        self.player_notebook = player_notebook                  # Dict

    ''' GETTER FUNCTIONS '''
    # Returns the player's status corresponding to actively playing, passively playing (lost), or unchosen
    def get_player_status(self):
        return self.player_status
    
    # Returns the player's notebook
    def get_notebook(self):
        return self.player_notebook

    # Returns the player's hand, Deck of Cards
    def get_hand(self):
        return self.player_hand
    
    
    ''' SETTER FUNCTIONS '''
    # Update the player's old location and current location
    def update(self, new_location):
        self.player_old_location = self.player_current_location
        self.player_current_location = new_location
    
    # Update the player's status
    def set_player_status(self, PLAYER_STATUS):
        self.player_status = PLAYER_STATUS
    
    # Update the player's turn status
    def set_player_status(self, TURN_STATUS):
        self.turn_status = TURN_STATUS