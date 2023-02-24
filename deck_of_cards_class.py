import random  # library for random number generation needed for shuffling a deck of cards.

# ----------CONSTANTS----------
SUITS = ["clubs", "diamonds", "hearts", "spades"]
NAMES = ['two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


class Card:
    # object to model an individual playing card.
    def __init__(self, name, suit, rank, value):
        # initialize the attributes of a playing card (name, suit, rank, and value).
        self.name = name
        self.suit = suit
        self.rank = rank
        self.value = value

    def get_name(self):
        # Return the simple name of the card
        return self.name

    def get_suit(self):
        # Return the suit of the card.
        return self.suit

    def get_rank(self):
        # Return the value of the card.
        return self.rank

    def get_value(self):
        # Return the value of the card.
        return self.value

    def display(self):
        # Display the descriptive name of a card including name and suit.
        print("{} of {}".format(self.name.title(), self.suit.title()))

    def debug_descriptive_name(self):
        # Display full card name as well as rank and value.  Used for debugging.
        print("{} of {} (R:{}, V:{})".format(self.name, self.suit, self.rank, self.value))


class Deck:
    # object to model a deck of playing cards.
    def __init__(self):
        # Initialize the deck.
        self.cards = []

    def populate(self):
        # Build the deck adding playing cards.
        for suit in SUITS:
            value = 0  # Initialize value for each suit
            rank = 2  # Initialize rank for each suit
            for name in NAMES:
                self.cards.append(Card(name, suit, rank, VALUES[value]))
                value += 1
                rank += 1

    def shuffle(self):
        # Shuffle deck by randomly swapping positions within the deck.
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        # Draw the last card from the deck.
        return self.cards.pop()

    def display(self):
        # Display the deck of playing cards.
        for c in self.cards:
            c.debug_descriptive_name()


deck = Deck()
deck.populate()
deck.shuffle()
myHand = []
count = len(deck.cards)

print(f"There are {count} cards in the deck")
print("Dealing 5 cards...\n")

for card in range(5):
    myHand.append(deck.draw_card())

for card in myHand:
    card.display()

count = len(myHand)

print(f"\nThere are {count} cards in your hand.")

count = len(deck.cards)

print(f"There are now {count} cards left in the deck\n")

countTwo, countThree, countFour, countFive, countSix, countSeven, countEight = 0, 0, 0, 0, 0, 0, 0
countNine, countTen, countJack, countQueen, countKing, countAce = 0, 0, 0, 0, 0, 0
countSpades, countHearts, countClubs, countDiamonds = 0, 0, 0, 0
countValue = 0

for card in myHand:
    countTwo += card.get_name().count('two')
    countThree += card.get_name().count('three')
    countFour += card.get_name().count('four')
    countFive += card.get_name().count('five')
    countSix += card.get_name().count('six')
    countSeven += card.get_name().count('seven')
    countEight += card.get_name().count('eight')
    countNine += card.get_name().count('nine')
    countTen += card.get_name().count('ten')
    countJack += card.get_name().count('jack')
    countQueen += card.get_name().count('queen')
    countKing += card.get_name().count('king')
    countAce += card.get_name().count('ace')
    countSpades += card.get_suit().count('spades')
    countHearts += card.get_suit().count('hearts')
    countClubs += card.get_suit().count('clubs')
    countDiamonds += card.get_suit().count('diamonds')
    countValue += card.get_value()

print("---The Contents of the Hand Dealt---")

print("CARDS:")
if countTwo > 0:
    print(f"There are {countTwo} twos in your hand")
if countThree > 0:
    print(f"There are {countThree} threes in your hand")
if countFour > 0:
    print(f"There are {countFour} fours in your hand")
if countFive > 0:
    print(f"There are {countFive} fives in your hand")
if countSix > 0:
    print(f"There are {countSix} sixes in your hand")
if countSeven > 0:
    print(f"There are {countSeven} sevens in your hand")
if countEight > 0:
    print(f"There are {countEight} eights in your hand")
if countNine > 0:
    print(f"There are {countNine} nines in your hand")
if countTen > 0:
    print(f"There are {countTen} tens in your hand")
if countJack > 0:
    print(f"There are {countJack} jacks in your hand")
if countQueen > 0:
    print(f"There are {countQueen} queens in your hand")
if countKing > 0:
    print(f"There are {countKing} kings in your hand")
if countAce > 0:
    print(f"There are {countAce} aces in your hand")

print("\nSUIT:")
if countSpades > 0:
    print(f"There are {countSpades} spades in your hand")
if countSpades == 5:
    print("You have a FLUSH made up of 5 Spades!!!")
if countHearts > 0:
    print(f"There are {countHearts} hearts in your hand")
if countHearts == 5:
    print("You have a FLUSH made up of 5 Hearts!!!")
if countClubs > 0:
    print(f"There are {countClubs} clubs in your hand")
if countClubs == 5:
    print("You have a FLUSH made up of 5 Clubs!!!")
if countDiamonds > 0:
    print(f"There are {countDiamonds} diamonds in your hand")
if countDiamonds == 5:
    print("You have a FLUSH made up of 5 Diamonds!!!")

print(f"\nVALUE of hand = {countValue}")
