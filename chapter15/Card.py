class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None,
              None,
              "2","3","4","5","6","7","8","9","10",
              "Jack","Queen","King","Ace"
              ]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        value = self.values[self.value] + " of " \
                + self.suits[self.suit]
        return value
