import random

# Card class represents a single card in the deck
class Card:
    def __init__(self, suit, rank):
        """
        Initialize a card with a suit (e.g., Hearts) and rank (e.g., 10, J, A)
        """
        self.suit = suit  # The suit of the card (Hearts, Spades, etc.)
        self.rank = rank  # The rank of the card (2-10, J, Q, K, A)
  
    def __str__(self):
        """
        Return a string representation of the card (e.g., '10 of Hearts')
        """
        return f'{self.rank} of {self.suit}'  # Format card as a string for display

# Deck class represents a collection of 52 cards
class Deck:
    def __init__(self):
        """
        Initialize the deck with 52 cards (13 ranks x 4 suits) and shuffle them
        """
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  # Four possible suits
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']  # Card ranks
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]  # Create all combinations of cards
        random.shuffle(self.cards)  # Shuffle the deck to randomize the card order

    def deal_card(self):
        """
        Deal a card by popping it from the deck and returning it
        """
        return self.cards.pop()  # Deal the card from the deck (last card in the list)

# Player class represents a player or the dealer in the game
class Player:
    def __init__(self, name):
        """
        Initialize a player with a name, an empty hand, and a score of 0
        """
        self.name = name  # Player's name (could be 'Player' or 'Dealer')
        self.hand = []  # List to store cards dealt to the player
        self.score = 0  # The player's score based on their hand
        self.ace_count = 0  # To track the number of aces in hand (since Aces can be worth 1 or 11)

    def add_card(self, card):
        """
        Add a card to the player's hand and update the score
        """
        self.hand.append(card)  # Add the card to the player's hand
        self.update_score(card)  # Update the player's score based on the card's value

    def update_score(self, card):
        """
        Update the player's score based on the card's rank
        """
        if card.rank.isdigit():
            self.score += int(card.rank)  # Number cards (2-10) add their face value to the score
        elif card.rank in ['J', 'Q', 'K']:
            self.score += 10  # Face cards (J, Q, K) are worth 10 points
        else:  # Ace handling
            self.score += 11  # Initially count an Ace as 11 points
            self.ace_count += 1  # Keep track of the number of Aces

        # If the score exceeds 21 and there is an Ace, count the Ace as 1 instead of 11
        while self.score > 21 and self.ace_count > 0:
            self.score -= 10  # Change an Ace from 11 points to 1 point
            self.ace_count -= 1  # Reduce the count of Aces treated as 11

    def show_hand(self, reveal_first_card=False, reveal_full_hand=False):
        """
        Return a string representation of the player's hand.
        For the dealer, optionally reveal only the first card or the full hand.
        """
        if reveal_first_card and not reveal_full_hand:
            # Show only the dealer's first card, hiding the rest
            hand_str = f'{self.hand[0]} and [hidden card]'
            return f'{self.name}\'s hand: {hand_str}'
        else:
            # Show all cards in the player's hand
            hand_str = ', '.join(str(card) for card in self.hand)
            return f'{self.name}\'s hand: {hand_str} (Score: {self.score})'

# Game class contains the main logic for playing a Blackjack game
class BlackjackGame:
    def __init__(self):
        """
        Initialize the game with a deck, a player, and a dealer
        """
        self.deck = Deck()  # Create a shuffled deck of 52 cards
        self.player = None  # The player will be initialized later after asking their name
        self.dealer = Player("Dealer")  # Initialize the dealer

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
        name = input("Please enter your name: ")  # Prompt the player to input their name
        self.player = Player(name)  # Create the player using the provided name

    def player_turn(self):
        """
        Handle the player's turn where they can hit (take more cards) or stand
        """
        while True:
            print(self.player.show_hand())  # Show the player's current hand and score
            choice = input("Do you want to hit or stay? (h/s): ").lower()  # Ask the player to hit or stay
            if choice == 'h':
                # Deal another card to the player if they choose to hit
                self.player.add_card(self.deck.deal_card())
                if self.player.score > 21:
                    print("Player busts!")  # If the player's score exceeds 21, they bust
                    break
            elif choice == 's':
                print("Player stays.")  # Player chooses to stop taking more cards
                break

    def dealer_turn(self):
        """
        Handle the dealer's turn. The dealer must hit until their score is 17 or higher
        """
        # Reveal the dealer's full hand once the player has completed their turn
        print(self.dealer.show_hand(reveal_full_hand=True))
        while self.dealer.score < 17:
            print("Dealer hits.")  # Dealer must hit if their score is below 17
            self.dealer.add_card(self.deck.deal_card())  # Deal a card to the dealer
            print(self.dealer.show_hand(reveal_full_hand=True))  # Show the updated dealer's hand
        if self.dealer.score > 21:
            print("Dealer busts!")  # If the dealer's score exceeds 21, they bust

    def determine_winner(self):
        """
        Determine the winner based on the player's and dealer's final scores
        """
        if self.player.score > 21:
            print(f"Dealer wins!")  # If the player busts, the dealer wins
        elif self.dealer.score > 21 or self.player.score > self.dealer.score:
            print(f"{self.player.name} wins!")  # The player wins if their score is higher or the dealer busts
        elif self.player.score < self.dealer.score:
            print("Dealer wins!")  # Dealer wins if their score is higher
        else:
            print("It's a tie!")  # The game is a tie if both scores are equal

    def play(self):
        """
        Main function to play the game: ask for player name, deal cards, take turns, and determine the winner
        """
        print("Welcome to Blackjack!")  # Welcome message
        self.ask_player_name()  # Ask for the player's name
        while True:
            # Reset deck, player hand, and scores at the beginning of each game
            self.deck = Deck()  # Reset the deck
            self.player.hand.clear()  # Clear player's hand
            self.player.score = 0  # Reset player's score
            self.dealer.hand.clear()  # Clear dealer's hand
            self.dealer.score = 0  # Reset dealer's score
            
            self.deal_initial_cards()  # Deal the initial two cards to each player
            
            # Show player's hand and dealer's first card (but not the full hand yet)
            print(self.player.show_hand())  # Show the player's current hand and score
            print(self.dealer.show_hand(reveal_first_card=True))  # Show only the dealer's first card
            
            self.player_turn()  # Handle the player's turn
            if self.player.score <= 21:
                self.dealer_turn()  # Handle the dealer's turn
            self.determine_winner()  # Determine and print the winner

            # Ask if the player wants to play again
            replay = input("Do you want to play again? (y/n): ").lower()
            if replay != 'y':
                print("Thanks for playing!")  # End the game if the player doesn't want to replay
                break

# Run the game
if __name__ == '__main__':
    game = BlackjackGame()  # Create a new BlackjackGame instance
    game.play()  # Start the game
