
import random
from replit import clear
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(logo)
def main():
  dealer_cards = []
  player_cards = []
  
  def start():
    dealer_cards.clear()
    player_cards.clear()
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if start == "y":
      clear()
      print(logo)
      blackjack()
    elif start == "n":
      print("Goodbye")
    else:
      print("Enter a valid keyword, please")
      main()

  
  
  def blackjack():
    dealer_cards.append(random.choice(cards))
    dealer_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    player_cards.append(random.choice(cards))
    option()

  def hands():
    print(f"Player's final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Dealer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
  
  def player_score():
    if 11 in player_cards:
      if sum(player_cards) > 21:
        print("Your ace now is 1!")
        i = player_cards.index(11)
        player_cards[i] = 1
    if sum(player_cards) > 21:
      print("You went over. You lose 😭")
      hands()
      start()
    elif sum(player_cards) == 21:
      print("You win 😃")
      hands()
      start()
    else:
      option()
      
  def dealer_score():
    while sum(dealer_cards) < 17:
      dealer_cards.append(deal_card())
    if 11 in dealer_cards:
      if sum(dealer_cards) > 21:
        print("Dealer's Ace is now 1")
        i = dealer_cards.index(11)
        dealer_cards[i] = 1
    if sum(dealer_cards) > 21:
      print("You win. Dealer went over 😁")
    elif sum(dealer_cards) == 21:
      print("You lose. Dealer has Blackjack 😱")
    elif sum(dealer_cards) > sum(player_cards):
      print("You lose 😤")
    elif sum(dealer_cards) == sum(player_cards):
      print("Draw!")
    else:
      print("You won 😁!")
    hands()
    start()
  
  def deal_card():
    return random.choice(cards)
  
  def option():
    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
    print(f"Computer's first card: {dealer_cards[0]}")
          
    option = input("Would you like to pick another card? Type 'y' or 'n': ")
    if option == "y":
      player_cards.append(deal_card())
      player_score()
    if option == "n":
      dealer_score()
      
  start()
main()
