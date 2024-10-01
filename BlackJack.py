import random # Import the random module to shuffle the deck

# Card class represents a single card in the deck
class Card:
  def __init__(self, suit, rank):
    """
    Initialize a card with a suit (e.g., Hearts) and rank (e.g., 10, J, A)
    """
    self.suit = suit # The suit of the card (e.g., Hearts, Spades)
    self.rank = rank # The rank of the card (e.g., 2, 3, 4, 10, J, Q, K. A)
  
  def __str__(self):
  """
  Return a string representaion of the card (e.g., '10 of hearts')
  """
  return f'{self.rank} of {self.suit}'

# Deck class represents a collection of 52 cards
class Deck:
  def __init__(self):
    """
    Intiialize the deck with 52 cards (13 ranks x 4 suits) and shuffle them
    """
    suits = ['Hearts' , 'Diamonds' , 'Clubs' , 'Spades'] #Four suits in the deck
    ranks = ['2' , '3' , '4' , '5', '6' , '7' , '8' , '9' ,'10' , 'J' , 'Q' , 'K' , 'A'] #Ranks 2-10, J, Q, K, A
    # Create a list of Card objects for all combinations of suits and ranks
    self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
   random.shuffle(self.cards) # Shuffle the deck to randomize the card order

def deal_card(self):
  """
  Deal a card by popping it from the deck and returning it
  """
  return self.cards.pop() #Removes and returns the last card from the deck
  
# Player class represents a player or the dealer in the game
class Player: 
  def __init__(self, name):
    """
    Initialize a player with a name, empty hand, and score of 0
    """
    self.name = name #Name of the player (e.g., 'Player' or 'Dealer')
    self.hand = [] # List to store the cards dealt to the player
    self.score = 0 # The current score (sum of card values) for the player 
    self.ace_count = 0 # Coint the number of aces in hand (Aces can be worth 1 0r 11)

def add_card(self, card):
  """
  Add a card to the player's hand and update the score
  """
  self.hand.append(card) # Add the card to the player's hand 
  self.update_score(card) # Update the player's score based on the card's value 

def update_score(self, card):
  """
  Update the player's score based on the card's rank 
  """
  if card.rank.isdigit(): #If the card is a number card (2-10)
    self.score += int(card.rank) # Add its face value to the score
  elif card.rank in ['J', 'Q', 'K']:
      self.score += 10   #Face cards are worth 10 points 
  else: # If card is an Ace
      self.score += 11 # Intially count Ace as 11 points 
      self.ace_count += 1 # one less ace counted as 11 points

def show_hand(self):
  """
  Return a string representation of the player's hand
  """
  hand_str = ', '.join(str(card) for card in self.hand) #Convert all cards to strings 
  return f'{self.name}\'s hand: {hand_str} (Score: {self.score})'

#Game class contains the main logic for playing a Blackjack game
class BlackjackGame:
  def __init__(self):
    """
    Intialize the game with a deck, a player, and a dealer
    """
    self.deck = Deck() #Create and shuffle a deck of cards
    self.player = Player("Player") # Create a Player
    self.dealer = Player("Dealer") # Create a dealer

def deal_initial_cards(self):
  """
  Deal two cards tp the player and the dealer at the start
  """
  for _ in range(2):
    self.player.add_card(self.deck.deal_card()) # Deal two cards to the player
    self.dealer.add_card(self.deck.deal_card()) # Deal two cards to the dealer

def player_tur(self):
  """
  Handle the player's turn where they can hit (take more cards) or stand
  """
  while True:
    print(self.player.show_hand()) # Show the player's current hand and score
    choice = input("Do you want to hit or stand? (h/s): ").lower() #Ask the player to hit or stand
    if self.player.score> 21: # If player's score exceeds 21, they bust
      print("Player bust!")
      break
elif choice == 's':#If player chooses to stand 
    print("Player stands.")
    break

def dealer_turn(self):
  """
  Handle the dealer's turn. The dealer must hit until their score is 17 or higher
  """
  print(self.dealer.show_hand()) #Show the dealer's initial hand
  while self.dealer.score < 17: #Dealer must hit if their score is below 17
  print("Dealer hits.")
  self.dealer.add_card(self.deck.deal_card()) #Deal a card to the dealer
print(self.dealer.show_hand()) # Show the updated dealer's hand
if self.dealer.score > 21: # If dealer's score exceeds 21, they bust
  print("Dealer busts!")

def determine_winner(self):
    """
    Determine the winner based on the player's and dealer's final scores
    """
    if self.player.score > 21:
      print("Dealer wins!")
    elif self.dealer.score > 21 or self.player.score > self.dealer.score:
      print ("Player wins!")
    elif self.player.score < self.dealer.score:
      print("Dealer wins!")
    else:
      print("It is a tie!")
def play(self):
      """
      Main function to play the game: deal cards, take turns, and determine the winner 
      """
  print("Welcome to Blackjack!")
  self.deal_initial_cards() # Deal the initial two cards to each player
  self.player_turn() #Handle the player's turn
  if self.player.score <= 21: # Only proceed to dealer's turn if the player hasn't busted
    self.dealer_turn() # Handle the dealer's turn
  self.determine_winner() # Determine and print the winner

# Run the game
if __name__ == '__main__':
  game = BlackjackGame() # Create a new BlackjackGame instance
  game.play() # Start the game 
