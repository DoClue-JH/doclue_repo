class Card:
    CARD_TYPES = {
        "character": ["Miss Scarlett", "Colonel Mustard", "Mrs. White", "Mr. Green", "Mrs. Peacock", "Professor Plum"],
        "room": ["Kitchen", "Ballroom", "Conservatory", "Dining Room", "Billiard Room", "Library", "Lounge", "Hall", "Study"],
        "weapon": ["Rope", "Lead Pipe", "Dagger", "Wrench", "Candlestick", "Revolver"]
    }

    def get_card_value(self, card):
        for card_type, cards in self.CARD_TYPES.items():
            if card in cards:
                return card

    def get_card_type(self, card):
        for card_type, cards in self.CARD_TYPES.items():
            if card in cards:
                return f"The card is a {card_type.capitalize()} type card"


# Driver code
# card = Card()
# card_name = "Ballroom"
# card_value = card.get_card_value(card_name)
# if card_value:
#     print(card_value)
# else:
#     print("This card does not exist")

# card_type = card.get_card_type(card_name)
# if card_type:
#     print(card_type)
# else:
#     print("Card type unknown")
