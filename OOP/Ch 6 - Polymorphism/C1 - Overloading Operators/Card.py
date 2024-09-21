import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __lt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index < other.suit_index
        return self.rank_index < other.suit_index

    def __gt__(self, other):
        if self.rank_index == other.rank_index:
            return self.suit_index > other.suit_index
        return self.rank_index > other.rank_index
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"