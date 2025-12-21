'''
PROBLEM: ACSL Rings is a 2-player game where the object is to score points by tossing a
ball through one of the 5 rings. Points are awarded as follows:
,
● Through the aqua or red ring - 1 point
● Through the orange or green ring - 3 points
● Through the black ring - 6 points
We will use a single letter to represent each of the colors:
aqua (A), red (R), orange (O), green (G), and black (B).
You will be given 2 strings representing each player’s results for all tosses that go through one of
the rings. Output a string containing each player’s score with the larger score first. If both players
have the same score, it doesn’t matter which one appears first.
EXAMPLE:

Input BRAG
BOB
Output 15 11
Explanation The first player’s tosses go through the black, red, aqua, and green rings,

and the player has a score of 6 + 1 + 1 + 3 = 11.
The second player’s tosses go through the black, orange, and black rings,
and the player has a score of 6 + 3 + 6 = 15.
Output is the string 15 11 with the larger score first.

INPUT: The input will consist of 2 strings as described above. Each string will be no more than
100 characters.
OUTPUT: Output the two scores separated by a single space with the larger score first.

2024-2025 ● Contest 1: Rings ● Junior Division

SAMPLE INPUT:
1. BRAG
BOB
2. AABBOOGG
BAROBA
3. GBORABORBA
BAAAAOORGGGB
4. OORRRGRBBRRAAABB
AAAAGRRRRGRRRBBOO
5. BARROGGBBGO
BBAAAARRRGGGOOOO
6. AAAABBBOOGGGRRR
RRBBOOOGGGAAAA

SAMPLE OUTPUT:
1. 15 11
2. 26 18
3. 32 31
4. 42 35
5. 40 36
6. 40 36

2024-2025 ● Contest 1: Rings ● Junior Division

TEST DATA

TEST INPUT:
1. AROBG
BRAGGROG
2. BOBBRAGROB
BARBAGGRAB
3. BBBAAAOOOGGGRRR
BBBBBAAAAGGGOOR
4. RRRRRRBBBBGGGGGGAAAO
AAAAAAOOOOOORRRBBBBB
5. BABAGORBABAGORBABAGORBABAGOR
GORBAGORBAGORBAGORBAGORBAGORBA
6. RRRGGGGBBBBAAOOOBBBAAARRBB
BBBBAAAAOOOOBBBGGGRRRGOAGOAGO
TEST OUTPUT:
1. 21 14
2. 36 29
3. 50 42
4. 57 54
5. 84 84
6. 90 85
'''


class Solution:

    # Define a function that takes two strings as input, each representing a player's ring toss results.
    def tosser(self, player_1, player_2):
        # create a dict for each ring thingy letter to its corresponding point value
        points = {'A': 1, 'R': 1, 'O': 3, 'G': 3, 'B': 6}
        # A and R → 1 point
        # O and G → 3 points
        # B → 6 points

        # Initialize two score counters, one for each player.
        score1, score2 = 0, 0

        # Loop through each character in the first player's string:
        for ring in player_1:
            score1 += points[ring]

        # Repeat the same loop for the second player's string to calculate their score.
        for ring in player_2:
            score2 += points[ring]
        # Compare the two scores:
        if score1 > score2:
            return f"{score1} {score2}"
        else:
            return f"{score2} {score1}"
        #   - If player 1 has a higher score, return their score first.
        #   - If player 2 has a higher score, return their score first.
        #   - If scores are equal, return them in any order.

        # Format the output as a string with the two scores separated by a space.


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]

    tests = [
        ("AROBG"
         , "BRAGGROG")
        , ("BOBBRAGROB"
           , "BARBAGGRAB")
        , ("BBBAAAOOOGGGRRR"
           , "BBBBBAAAAGGGOOR")
        , ("RRRRRRBBBBGGGGGGAAAO"
           , "AAAAAAOOOOOORRRBBBBB")
        , ("BABAGORBABAGORBABAGORBABAGOR"
           , "GORBAGORBAGORBAGORBAGORBAGORBA")
        , ("RRRGGGGBBBBAAOOOBBBAAARRBB"
           , "BBBBAAAAOOOOBBBGGGRRRGOAGOAGO")]
    outputs = [(21, 14)
        , (36, 29)
        , (50, 42)
        , (57, 54)
        , (84, 84)
        , (90, 85)]
    for i in range(len(tests)):
        p1, p2 = tests[i]
        answer = sol.tosser(p1, p2)
        s1, s2 = outputs[i]  # unpack
        if answer == f"{s1} {s2}":
            print(answer)
            print("👍👏Yippeee")
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
