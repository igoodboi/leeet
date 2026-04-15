"""
Kings in the Corners is a one-person card game that uses a standard deck of 52 playing cards.
The game begins with four cards placed face-up on the board, forming four original piles.
Four additional corner piles are empty at the start. The player receives a hand of cards.
The player attempts to play cards from the hand onto one of the 8 piles, each time, examining cards from left to right. The first playable card is moved according to these rules:
• If the card is a King, it is played onto the next available corner pile.
The corner piles are filled in a clockwise order, starting with the upper right corner.
• If the card is not a King, check the piles in clockwise order, starting with the topmost.
A card can be placed on a pile if it is the opposite color and one rank lower than the pile's top card.
For example, a 4 of Clubs can be played on either a 5 of Hearts or a 5 of Diamonds.
The game ends when no more cards can be played from the hand.
At the end of the game, print the top card on each of the 8 piles, starting from the topmost pile and proceeding clockwise. If a pile is empty, print "E".
Separate each card with a single space.
Each card is represented by a 2-character string: rank followed by suit.
The ranks, from high to low, are: K (king), Q (queen), J (jack), T (ten), 9, 8, 7, 6, 5, 4, 3, 2, and A (ace).
The suits are C (clubs), D (diamonds), H (hearts), and S (spades). Clubs and Spades are black; Diamonds and Hearts are red.
The image above shows the board after playing the following cards: 4C, 3D, KH, 8S.
EXAMPLE:
Input
3D 4C JH KH 8S
9H 5S 5H
QD

Output
8S KH
5s
3D E QD
E
Explanation
Cards are played as follows:


Card
Played
Player's hand
Top card on each pile


3D 4C JH KH
8 S
9H E 5S
E
5H E QD E

4C
3D
JH KH 8S
9H E 5S
E
4C E QD E

3D
JH KH 8S
9H E 5S E
3D E QD E


JH 8S
9H KH 5S E 3D E QD

8S
JH
8S KH 5S E 3D E QD E
At this point, the last card cannot be played on any pile so the game ends.
Output the top card on each pile: 8S KH 5S E 3D E QD E
TASK:
Complete the function playCards
• The function has 2 parameters: a string, hand, for the cards in the player's hand, and a string, piles, for the cards placed face-up to start the 4 initial piles.
For each string, each card is separated by a single space and uses a 2-character format as described above.
• The function returns a string of the top card on each pile starting with the topmost moving clockwise using the letter "E" if it is empty, each separated by a single space.
You may create additional functions that are called from playCards if needed in solving the problem.
CONSTRAINTS:
20 cards.
There will be no duplicate cards and no Kings placed at the beginning of the game. The player's hand will contain no more than
DATA PROVIDED:
There are 6 sets of Sample Data for debugging and 6 sets of Test Data for scoring. The test cases will vary in difficulty.
You should create sample data of your own to fully test your program.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'playCards' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING hand
#  2. STRING piles
#
def preporc(string) -> list:
    # return a list of (point,color) point is int, color is "r" or "b"
    pass


def playCards(hand, piles):
    # Write your code here
    # JC 5C 7D QD KC 8S KS
    # 6C 7S 6H 9H
    # step one pre-processing
    hand = preporc(hand)
    piles = preporc(piles)
    corners = [None] * 4
    # play
    while hand:
        playable = False
        num = 0
        for card in hand:
            if card[0] == 13:
                for i in range(4):
                    j = (num + i) % 4
                    corners.append(card)
            else:
                for p in range(len(piles)):
                    desk = piles[p]
                    if desk[0] - card[0] == 1 and card[1] != desk[1]:
                        piles[p] = card
                        playable = True

            # smack it down

    # format, return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    hand = "JC 5C 7D QD KC 8S KS"

    piles = "6C 7S 6H 9H"

    result = playCards(hand, piles)

    fptr.write(result + '\n')

    fptr.close()
