import random

class Deck:
    def __init__(self):
        self.cards = []

        shapes = ['hearts', 'diamonds', 'spades', 'clubs']

        ranks = [
            {"rank": "A", "value": 11},
            {"rank": 2, "value": 2},
            {"rank": 3, "value": 3},
            {"rank": 4, "value": 4},
            {"rank": 5, "value": 5},
            {"rank": 6, "value": 6},
            {"rank": 7, "value": 7},
            {"rank": 8, "value": 8},
            {"rank": 9, "value": 9},
            {"rank": 10, "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "K", "value": 10},
            {"rank": "Q", "value": 10},
        ]

        for shape in shapes:
            for rank in ranks:
                self.cards.append({"shape": shape, "rank": rank["rank"], "value": rank["value"]})


    def shuffle_cards(self):
        if(len(self.cards)> 1):
            random.shuffle(self.cards)

    def deal(self, numbers):
        cards_dealt = []
        for _ in range(numbers):
                if(len(self.cards) > 0):
                    cards_dealt.append(self.cards.pop())
        return cards_dealt

    def __str__(self):
        return f"Deck with {len(self.cards)} cards"

# Example usage:
deck1 = Deck()
print(deck1)  # Deck with 52 cards
print(deck1.deal(5))  # Deal 5 cards
