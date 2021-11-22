'''
Tom Lazore
Lab 9 BlackJack
This program simulates a black jack game between two players. Cards are dealt until one player goes past 21 in value.
'''


import random

print('Welcome to my Black Jack program!')
print('The first player to go over 21 loses')
print('First enter your names\n')

player1Name = input('Player 1, What is your name? ')
player2Name = input('Player 2, What is your name? ')
print()

def main():#Main Function to play game
    player1 = 0
    player2 = 0
    deck = createDeck()

    numCards = 2
    dealNumber = 1
    
    print('Deal',dealNumber)
    print(player1Name,'Draws 2 Cards...')
    player1 = dealCards(deck,numCards,player1)
    print(player1Name + "'s Score:",player1)
    print()
    print(player2Name,'Draws 2 Cards...')
    player2 = dealCards(deck,numCards,player2)
    print(player2Name + "'s Score:",player2)
    print()

    cardCount = 48  
    while cardCount > 0:#deals until all cards are gone

        if player1 < 21 and player2 < 21:
            numCards = 1
            dealNumber +=1
            print('Deal',dealNumber)
            print(player1Name,'Draws Another Card')
            player1 = dealCards(deck,numCards,player1)
            cardCount-=1
            if player1 == 11:#changes ace value to a 1
                aceValue = input('Do you want to change the value of the Ace to a 1? ')
                if aceValue == 'y':
                    player1 -= 10
            print(player1Name + "'s Score:",player1)
            print()
            print(player2Name,'Draws Another Card')
            player2 = dealCards(deck,numCards,player2)
            cardCount-=1
            print(player2Name + "'s Score:",player2)
            if player2 == 11:
                aceValue = input('Do you want to change the value of the Ace to a 1? ')
                if aceValue == 'y':
                    player2 -= 10
            print()
            #Different outcomes of the game
            if player1 > 21 and player2 > 21:
                print(player1Name,'and',player2Name,'both busted!')

            elif player1 > 21:
                print(player1Name,'busted!', player2Name,'Wins!')

            elif player2 > 21:
                print(player2Name,'busted!',player1Name,'Wins!')

            elif player1 == 21 and player2 == 21:
                print('You both win!')

            elif player1 == 21:
                print(player1Name, 'hit 21! You win!')

            elif player2 == 21:
                print(player2Name,'hit 21! You win!')
  


def createDeck():#Creates deck of cards
    
    deck = {'Ace of Spades':11, '2 of Spades':2, '3 of Spades':3,
        '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
        '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
        '10 of Spades':10, 'Jack of Spades':10,'Queen of Spades':10, 'King of Spades': 10,

        'Ace of Hearts':11, '2 of Hearts':2, '3 of Hearts':3,'4 of Hearts':4,
        '5 of Hearts':5, '6 of Hearts':6,'7 of Hearts':7, '8 of Hearts':8,
        '9 of Hearts':9,'10 of Hearts':10, 'Jack of Hearts':10,'Queen of Hearts':10, 'King of Hearts': 10,

        'Ace of Clubs':11, '2 of Clubs':2, '3 of Clubs':3,'4 of Clubs':4, '5 of Clubs':5,
        '6 of Clubs':6,'7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,'10 of Clubs':10,
        'Jack of Clubs':10,'Queen of Clubs':10, 'King of Clubs': 10,

        'Ace of Diamonds':11, '2 of Diamonds':2, '3 of Diamonds':3,'4 of Diamonds':4, '5 of Diamonds':5,
        '6 of Diamonds':6,'7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,'10 of Diamonds':10,
        'Jack of Diamonds':10,'Queen of Diamonds':10, 'King of Diamonds':10}
    
    return deck

def dealCards(deck,numCards,handValue):#Generates cards to deal and their total value
    

    for count in range(numCards):
        rank,suit = random.choice(list(deck.items()))
        handValue = handValue + suit
        print(rank)
    return handValue 
    
main()



 

        
            

    
                   
