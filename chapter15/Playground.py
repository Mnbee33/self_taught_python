import Card
import Deck

card1 = Card.Card(10, 2)
card2 = Card.Card(11, 3)
print(card1 < card2)
print(card1 > card2)
print(card1)

deck = Deck.Deck()
for card in deck.cards:
    print(card)
