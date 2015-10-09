# Nathan Pugh Collaberated with Josiah Hardacre, Trevor waite
# CIS 125-82A
# October 7, 2015
# Week 5 Lab

import random	

def main():
	"""
	Deck, PlayerAHand and PlayerBHand are all lists
	"""
	
	Deck = []
	PlayerAHand = []
	PlayerBHand = []
	gameCounter = 0

	# Create deck.  Cards are represented by an integer value
	for i in range(52):
		Deck.append(i)
	
	# Shuffle the deck
	random.shuffle(Deck)
	
	# Deal 1/2 the cards to each player
	for x in range(26):
		PlayerAHand.append(Deck.pop())
		PlayerBHand.append(Deck.pop())
	
	# Main Gameplay
		
	while len(PlayerAHand) > 0 and len(PlayerBHand) > 0:
		gameCounter += 1
		PlayerAHand, PlayerBHand = playRound(PlayerAHand, PlayerBHand)
	
	# End of game
	
	print("There were ", gameCounter, " rounds played")

def playRound(PlayerA, PlayerB):
	Acard = PlayerA.pop()
	Bcard = PlayerB.pop()
	
	Arank = getRank(Acard)
	Brank = getRank(Bcard)
	
	if Arank > Brank:
		PlayerA.insert(0, Acard)
	elif Brank > Arank:
		PlayerB.insert(0, Bcard)
	else:
		PlayerA, PlayerB = WAR(PlayerA, PlayerB)
	
	'''
	This is the method that plays one round of War
	The method takes PlayerA and PlayerB as input parameters
	and returns PlayerA and PlayerB after modification
	for the round
	
	Remember, high card wins. I have included a convenience
	function getRank(anyCard) that will return the rank.
	
	See the README.md for the variations of
	the game to program.
	'''
	return PlayerA, PlayerB


def WAR(PlayerA, PlayerB):
	# See the README.md file for instructions on coding 
	# This module.

	return PlayerA, PlayerB

	
def getRank(anyCard):
	return anyCard % 13


if __name__ == '__main__':
	main()

