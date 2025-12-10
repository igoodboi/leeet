'''
PROBLEM: ACSL Tiles is a one-person game played with rectangular tiles. Each tile has a
single-digit number between 1 and 9 inclusive at each end. At the start of the game, there are 4
rows, each with a number. The goal of the game is to build rows by placing a tile at the right end
of the topmost row whose last number matches a number on the tile. Tiles can be re-oriented;
thus, the tiles 34 and 43 are the same tile. If a tile cannot be placed on any row, it is placed in the
discard pile. When all tiles have been played or discarded, find the sum of the single-digit
numbers on all of the tiles in the discard pile.
EXAMPLE:
Input:
5923
56 85 27 73 14 34 62
Output:
18
Explanation:
The game starts with 4 rows having numbers 5, 9, 2, 3.

After tile 56 is placed in Row 1, tile 85 is placed in the discard pile. Both 27 and 73 are placed
in Row 3 and tile 14 is placed in the discard pile.

The next tile, 34, is placed in Row 3, the topmost row it can go on. And finally, the 26 tile is
added to Row 1, with the orientation of 62. The result is as follows:

2023-2024 ● Contest 1: ACSL Tiles ● Junior Division

The result is the sum of 8+5+1+4=18.
INPUT: Input a 4-digit integer that gives the initial numbers from Row 1 to Row 4, and a string
of no more than fifty 2-digit integers, each separated by a single space. Each 2-digit integer
represents the two numbers on each tile, both between 1 and 9, inclusive.
OUTPUT: After placing the tiles using the rules above, output the sum of the single-digit
numbers on all of the tiles in the discard pile.
SAMPLE INPUT:
1. 5923
56 85 27 73 14 34 62
2. 8423
74 92 57 93 26 87 14 63 82 54 12
3. 1253
51 81 35 84 95 26 59 13 71 35 46 28
4. 2694
69 76 41 89 16 78 64 36 12 95 52
5. 6479
58 73 92 54 75 35 78 25 81 24 16 95 36 82 14 27 43 13 51
SAMPLE OUTPUT:
1. 18
2. 26
3. 31
4. 22
5. 45

2023-2024 ● Contest 1: ACSL Tiles ● Junior Division

TEST DATA

TEST INPUT:
1. 3972
18 17 65 61 37 51 57 38 72 92 54 59 43 41 31 28
2. 9146
95 74 51 19 75 26 32 39 35 31 25 73
3. 7918
63 18 56 98 48 52 26 92 83 13 17 58 91 67 58
4. 9758
52 14 51 27 77 62 76 82 96 56 46 49 87
5. 7169
71 56 15 65 98 71 89 71 11 55 77 17 66 51

TEST OUTPUT:
1. 56
2. 0
3. 59
4. 48
5. 14
'''


class Solution:
    def arrange(self, rows, tiles):
        def split(num) -> int:
            digits = []

            while num != 0:
                # do modulo to the num to get the ramiander
                # get rid of the remainder by dividing by 10
                d = num % 10
                num = num // 10
                digits.append(d)
            return digits[::-1]

        # split the rows to rows
        rowz = split(rows)
        # go through list see if it matches
        discard = []
        for tile in tiles:
            found = False
            # if it doesn't go to the next until [-1]
            for i in range(len(rowz)):
                t = str(tile)
                # if it does match it
                if str(rowz[i]) == t[0]:
                    rowz[i] = int(t[1])
                    found = True
                    break
                elif str(rowz[i]) == t[1]:
                    rowz[i] = int(t[0])
                    found = True
                    break
            # if it doesn't match put it in discard.
            if not found:
                discard.append(tile)
            # do that w/ all of them

        # see discard pile split the nums to single digit.
        total = 0
        for k in range(len(discard)):
            digits = split(discard[k])
            for d in digits:
                total += d
                # add em up

        # return
        return total


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    tests = [[3972, 18, 17, 65, 61, 37, 51, 57, 38, 72, 92, 54, 59, 43, 41, 31, 28],
             [9146, 95, 74, 51, 19, 75, 26, 32, 39, 35, 31, 25, 73],
             [7918, 63, 18, 56, 98, 48, 52, 26, 92, 83, 13, 17, 58, 91, 67, 58],
             [9758, 52, 14, 51, 27, 77, 62, 76, 82, 96, 56, 46, 49, 87],
             [7169, 71, 56, 15, 65, 98, 71, 89, 71, 11, 55, 77, 17, 66, 51]
             ]
    outputs = [56, 0, 59, 48, 14]
    for i in range(len(tests)):
        test = tests[i]
        rows = test[0]
        tiles = test[1:]
        print(rows, tiles)
        answer = sol.arrange(rows, tiles)
        if answer == outputs[i]:
            print("👍👏Yippeee")
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
