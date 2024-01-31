import random
import art
import os
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.√

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().√

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.√

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.√

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.√


#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17. √

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.√

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


def deal_card():
	cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
	return random.choice(cards)

def calculate_score(hand):
	if sum(hand) == 21 and len(hand) == 2:
		return 0
	if 11 in hand and sum(hand) > 21:
		hand.remove(11)
		hand.append(1)
		print("Value in hand, changed to a 1")
		print(hand)
	if sum(hand) <= 21:
		return sum(hand)
	else:
		return float('inf')  

def computer_play(hand):
	while calculate_score(hand) != 0 and calculate_score(hand) <= 17 and calculate_score(hand) != float('inf'):
		hand.append(deal_card())
	return calculate_score(hand)

def compare(user_score, comp_score):
    if user_score == 0:
        return "User got blackjack, they win"
    elif comp_score == 0:
        return "Computer got blackjack, they win"
    elif user_score != float('inf') and comp_score != float('inf'):
        if user_score < comp_score:
            return "Computer wins!"
        elif user_score > comp_score:
            return "User wins"
        else:
            return "Draw"
    elif user_score == float('inf') and comp_score != float('inf'):
        return "Computer wins!"
    elif user_score != float('inf') and comp_score == float('inf'):
        return "User wins"
    else:
        return "Draw"

def clear_console():
	os.system('cls' if os.name == 'nt' else 'clear')
	art.print_logo()

	
def main():
	game_state = "Y"
	
	while game_state.lower() == "y":
		clear_console()
		user_cards = []
		computer_cards = []

		user_cards.append(deal_card())
		user_cards.append(deal_card())

		computer_cards.append(deal_card())
		computer_cards.append(deal_card())
		
		user_score = calculate_score(user_cards)
		comp_score = calculate_score(computer_cards)
		
		print("Your current score is " + str(user_score))
		print("Computer's current score is " + str(comp_score))
		
		user_input = input("Would you like another card: ")
		
		while user_input.lower() == "y":
			user_cards.append(deal_card()) 
			user_score = calculate_score(user_cards)
			if user_score == float('inf'):
				print("Game Over!")
				break
			else:    
				print("Your current score is " + str(user_score))
			user_input = input("Would you like another card? ")
		
		comp_score = computer_play(computer_cards)    
		
		print("Your final score is " + str(user_score))
		print("Computer's final score is " + str(comp_score))
		print(compare(user_score, comp_score))
		game_state = input("Would you like to play again? ")

if __name__ == "__main__":
	main()
