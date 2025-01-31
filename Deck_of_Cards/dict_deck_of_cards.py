# deck_of_cards.py
#
# 12/28/2020
#
# Rob Flemen
#
# Build a deck of playing cards in a list the a dictionary and print the deck

# Common code needed for all programs iterations - BEGIN
card_suit=['hearts', 'diamonds', 'clubs', 'spades']
card_name=['two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace']
card_value=[2,3,4,5,6,7,8,9,10,10,10,10,11]
k=0
# Common code needed for all programs iterations - END

# Code for using list - BEGIN
#deck=[None]*52
#for i in range (0,4):
#	for j in range (0,13):
#		deck[k]=[{card_name[j]},{card_suit[i]},{card_value[j]}]
#		k+=1
		
#print(deck)
# Code for using list - END

# Code needed for using dictionary - BEGIN
deck_of_cards = []

k=1

for card_var_i in range(4):
	for card_var_j in range(13):
		new_card = {'suit': card_suit[card_var_i], 'name': card_name[card_var_j], 'value': card_value[card_var_j]}
		deck_of_cards.append(new_card)

for card in deck_of_cards:
	print(f"{k} - the {card['name']} of {card['suit']} is worth {card['value']}!")
	k+=1
# Code needed for using dictionary - END

#print(deck_of_cards[0].get('suit'), deck_of_cards[50].get('suit'))
