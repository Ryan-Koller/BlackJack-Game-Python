import random

# Card class represents a single card in the deck
class Card:
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit (e.g., Hearts) and rank (e.g., 10, J, A)
        """
        self.suit = suit
        self.rank = rank
  
    def __str__(self):
        """
        Return a string representation of the card (e.g., '10 of Hearts')
        """
        return f'{self.rank} of {self.suit}'

# Deck class represents a collection of 52 cards
class Deck:
    def __init__(self):
        """
        Initialize the deck with 52 cards (13 ranks x 4 suits) and shuffle them
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)

    def deal_card(self):
        """
        Deal a card by popping it from the deck and returning it
        """
        return self.cards.pop()

# Player class represents a player or the dealer in the game
class Player:
    def __init__(self, name):
        """
        Initialize a player with a name, an empty hand, and a score of 0
        """
        self.name = name
        self.hand = []
        self.score = 0
        self.ace_count = 0

    def add_card(self, card):
        """
        Add a card to the player's hand and update the score
        """
        self.hand.append(card)
        self.update_score(card)

    def update_score(self, card):
        """
        Update the player's score based on the card's rank
        """
        if card.rank.isdigit():
            self.score += int(card.rank)
        elif card.rank in ['J', 'Q', 'K']:
            self.score += 10
        else:  # Ace
            self.score += 11
            self.ace_count += 1

        # Handle ace adjustment if score goes over 21
        while self.score > 21 and self.ace_count > 0:
            self.score -= 10
            self.ace_count -= 1

    def show_hand(self, reveal_first_card=False):
        """
        Return a string representation of the player's hand.
        Optionally hide all cards except the first one for the dealer.
        """
        if reveal_first_card:
            hand_str = f'{self.hand[0]} and [hidden card]'
        else:
            hand_str = ', '.join(str(card) for card in self.hand)
        return f'{self.name}\'s hand: {hand_str} (Score: {self.score})'

# Game class contains the main logic for playing a Blackjack game
class BlackjackGame:
    def __init__(self):
        """
        Initialize the game with a deck, a player, and a dealer
        """
        self.deck = Deck()
        self.player = None  # Will be initialized later
        self.dealer = Player("Dealer")

    def deal_initial_cards(self):
        """
        Deal two cards to the player and the dealer alternately
        """
        # Deal the first card to both the player and the dealer
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())
        
        # Deal the second card to both the player and the dealer
        self.player.add_card(self.deck.deal_card())
        self.dealer.add_card(self.deck.deal_card())

    def ask_player_name(self):
        """
        Ask the user for their name and create a Player object
        """
        name = input("Please enter your name: ")
        self.player = Player(name)

    def player_turn(self):
        """
        Handle the player's turn where they can hit (take more cards) or stand
        """
        while True:
            print(self.player.show_hand())  # Show the player's current hand and score
            choice = input("Do you want to hit or stay? (h/s): ").lower()
            if choice == 'h':
                self.player.add_card(self.deck.deal_card())  # Deal another card to the player
                if self.player.score > 21:
                    print("Player busts!")
                    break
            elif choice == 's':
                print("Player stays.")
                break

    def dealer_turn(self):
        """
        Handle the dealer's turn. The dealer must hit until their score is 17 or higher
        """
        print(self.dealer.show_hand(reveal_first_card=False))  # Show the dealer's full hand
        while self.dealer.score < 17:
            print("Dealer hits.")
            self.dealer.add_card(self.deck.deal_card())  # Deal a card to the dealer
            print(self.dealer.show_hand())  # Show the updated dealer's hand
        if self.dealer.score > 21:
            print("Dealer busts!")

    def determine_winner(self):
        """
        Determine the winner based on the player's and dealer's final scores
        """
        if self.player.score > 21:
            print(f"Dealer wins!")
        elif self.dealer.score > 21 or self.player.score > self.dealer.score:
            print(f"{self.player.name} wins!")
        elif self.player.score < self.dealer.score:
            print("Dealer wins!")
        else:
            print("It's a tie!")

    def play(self):
        """
        Main function to play the game: ask for player name, deal cards, take turns, and determine the winner
        """
        print("Welcome to Blackjack!")
        self.ask_player_name()  # Ask for the player's name
        self.deal_initial_cards()  # Deal the initial two cards to each player
        
        # Show player's hand and dealer's first card
        print(self.player.show_hand())  # Show the player's current hand and score
        print(self.dealer.show_hand(reveal_first_card=True))  # Show only the dealer's first card
        
        self.player_turn()  # Handle the player's turn
        if self.player.score <= 21:
            self.dealer_turn()  # Handle the dealer's turn
        self.determine_winner()  # Determine and print the winner

# Run the game
if __name__ == '__main__':
    game = BlackjackGame()  # Create a new BlackjackGame instance
    game.play()  # Start the game
