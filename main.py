import random
import art
import os


print(art.logo)

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
#11 is the Ace.

def clear(): #Clearing the screen for a new game
  os.system('clear')

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(card_list):  
  if 11 in card_list and 10 in card_list: #checking if the hand is a blackjack (Ace and 10, Jack, Queen, or King)
    return 0
  elif sum(card_list) > 21 and 11 in card_list: #If the hand is over 21, but has an Ace, we'll make the Ace = to 1 instead
    card_list.remove(11)
    card_list.append(1)
  else:
    return sum(card_list) #Takes a list of cards and calculates their sum per house rules

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has blackjack."
  elif user_score == 0:
    return "You got blackjack, you win!"
  elif user_score > 21:
    return "You bust."
  elif computer_score > 21:
    return "You win, computer bust."
  elif user_score > computer_score:
    return "You win with the higher score!"
  else:
    return "You lose with the lower score."
    
def play_game():
  user_cards = []
  computer_cards = []
  game_over = False
  
  for _ in range(2):  #dealing 2 cards to the players
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  
  while not game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, current score: {user_score}")
    print(f"  Computer's first card: {computer_cards[0]}")
    
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
    else:
      user_should_deal = input("Would you like another card? Type 'y' for yes or 'n' for no: ")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
  
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"  Your final hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game? of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()

