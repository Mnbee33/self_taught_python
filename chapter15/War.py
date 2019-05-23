import Deck
import Player

class Game:
    def __init__(self):
        name1 = input("player1's name: ")
        name2 = input("player2's name: ")
        self.deck = Deck.Deck()
        self.player1 = Player.Player(name1)
        self.player2 = Player.Player(name2)

    def wins(self, winner):
        w = "In this round, {} won."
        print(w.format(winner.name))

    def show_card(self, p1, p2):
        d = "{} drawed {}, and {} drawed {}."
        print(d.format(p1.name, p1.card, p2.name, p2.card))

    def play_game(self):
        cards = self.deck.cards
        print("the war starts")

        while len(cards) >= 2:
            message = "Type q to exit. Type other key to play: "
            resoponse = input(message)

            if resoponse == "q":
                break

            p1_card = self.deck.draw_card()
            self.player1.card = p1_card
            
            p2_card = self.deck.draw_card()
            self.player2.card = p2_card

            self.show_card(self.player1, self.player2)

            if p1_card > p2_card:
                self.player1.wins += 1
                self.wins(self.player1)
            else:
                self.player2.wins += 1
                self.wins(self.player2)

        win = self.winner(self.player1, self.player2)
        print("game set. {} won!".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "Even! Both"

war_game = Game()
war_game.play_game()
