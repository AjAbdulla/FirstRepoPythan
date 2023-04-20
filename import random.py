import random 

User1 = input ("What is your name?")
User2 = input ("What is your name ?")

card_names= ['A', '2', '3', '4','5','6', '7', '8', '9', '10', '11', '12', '13', '14' ]
#Name: shuffled deck 
#purpose: return a shuffled deck to user
#input: None
#output: list representing a shuffled deck 
def shuffled_deck():
    basic_deck= list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck

    def card_name(card):
        