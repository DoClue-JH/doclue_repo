import random
from Card import Card

class ClueDeck:
    def __init__(self, players):
        self.players = players
        self.card = Card() # Create an instance of the Card class

        # Choose one random character, room, and weapon for the secret deck
        self.secret_deck = [
            self.card.get_card_value(self.card.CARD_TYPES['character'][random.randint(0, len(self.card.CARD_TYPES['character'])-1)]),
            self.card.get_card_value(self.card.CARD_TYPES['room'][random.randint(0, len(self.card.CARD_TYPES['room'])-1)]),
            self.card.get_card_value(self.card.CARD_TYPES['weapon'][random.randint(0, len(self.card.CARD_TYPES['weapon'])-1)])
        ]
        # Remove secret deck cards from the remaining deck (self.deck)
        self.deck = [card for card in (self.card.CARD_TYPES['character'] + self.card.CARD_TYPES['room'] + self.card.CARD_TYPES['weapon']) if card not in self.secret_deck]
        random.shuffle(self.deck)

    # Deal out cards to players 
    def deal(self):
        num_players = len(self.players)
        
        # Create dictionary to hold dealt cards for each player
        dealt_cards = {}
        for i in range(num_players):
            dealt_cards[self.players[i]] = []

        # Deal cards to players
        for i in range(num_players):
            for player in dealt_cards:
                if len(self.deck) == 0:
                    break
                card = self.deck.pop(0)
                dealt_cards[player].append(card)

        # Deal remaining cards in round-robin fashion
        i = 0
        while len(self.deck) > 0:
            player = list(dealt_cards.keys())[i]
            card = self.deck.pop(0)
            dealt_cards[player].append(card)
            i = (i+1) % num_players
        
        # Return a dictionary in the format of player: [dealt cards]
        return dealt_cards

    def compare_deck(self, deck1, deck2):
        
        # Convert the decks to sets for faster comparison
        set_deck1 = set(deck1)
        set_deck2 = set(deck2)
        
        # Find matching cards
        matching_cards = [card for card in set_deck1.intersection(set_deck2)]

        return f"There are {len(matching_cards)} matching cards: {matching_cards}"
        
    # A method to output the functions in a deck
    def get_deck(self, deck):
            return deck.copy()

#Note that this class is called in Game.py