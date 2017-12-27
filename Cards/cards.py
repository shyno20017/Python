import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def lines(n):
    for x in range(n):
        print()

class Card:
    HEARTS = 0
    SPADES = 1
    DIAMONDS = 2
    CLUBS = 3
    suits = [x for x in range(4)]

    A = 1
    J = 11
    Q = 12
    K = 13
    ranks = [x for x in range(1, 14)]

    def __init__(self, suit, rank):
        if suit not in Card.suits:
            raise ValueError("Invaid suit")
        elif rank not in Card.ranks:
            raise ValueError("Invalid rank")
        else:
            self.suit = suit
            self.rank = rank

    def __str__(self):
        ret = ''
        if self.rank == 1:
            ret += 'A'
        elif self.rank == 11:
            ret += 'J'
        elif self.rank == 12:
            ret += 'Q'
        elif self.rank == 13:
            ret += 'K'
        else:
            ret += str(self.rank)

        ret += ' of '

        if self.suit == 0:
            ret += 'hearts'
        elif self.suit == 1:
            ret += 'clubs'
        elif self.suit == 2:
            ret += 'diamonds'
        else:
            ret += 'spades'

        return ret

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


class Deck:
    def __init__(self, cards=None):
        if cards is None:
            self.cards = []
            for suit in Card.suits:
                for rank in Card.ranks:
                    self.cards.append(Card(suit, rank))
        else:
            self.cards = cards

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self, n=1):
        if n == 1:
            return self.cards.pop(0)

        cards = []
        for x in range(n):
            cards.append(self.cards.pop(0))

        return Deck(cards)

    def add_card(self, card):
        if not self.contains_card(card):
            self.cards.append(card)

    def add_cards(self, cards):
        for card in cards:
            self.add_card(card)

    def contains_card(self, card):
        return card in self.cards

    def get_card(self, card):
        if not self.contains_card(card):
            return None

        for x, c in enumerate(self.cards):
            if card == c:
                return self.cards.pop(x)


    def __str__(self):
        return '[' + ', '.join(map(lambda card: str(card), self.cards)) + ']'

    def __iter__(self):
        return iter(self.cards)


class Hand(Deck):
    def __init__(self, name=''):
        self.name = name
        self.cards = []

    def __str__(self):
        if self.name:
            return self.name + '\'s hand: [' + ', '.join(map(lambda card: str(card), self.cards)) + ']'
        else:
            return '[' + ', '.join(map(lambda card: str(card), self.cards)) + ']'


deck = Deck()
hand = Hand("Shyno")
cls()
