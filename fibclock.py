'''
2021-2022 ● Contest 1: Fibonacci Clock ● Junior Division

PROBLEM: ACSL’s version of Philippe Chretien’s
“Fibonacci Clock” displays time by changing the
colors displayed in 5 squares, whose side lengths
correspond to the first 5 Fibonacci numbers (1, 1, 2,
3, and 5). Given the colors of the squares on the clock
face, you must output the time that is represented in
hh:mm format. The colors will be given to you as 5
individual characters representing the lower 1x1
square, the upper 1x1 square, the 2x2 square, the 3x3
square, and the 5x5 square in that order. (See
https://basbrun.com/2015/05/04/fibonacci-clock/.)
Red squares are used to represent only hours and green squares are used to represent only
minutes. Blue squares are used to represent both hours and minutes. White squares are ignored.
To find the current hour, add the values of the red and blue squares. To find the current minutes,
add the values of the green and blue squares and multiply by 5. The minutes are displayed in
five-minute increments.
The clock in the picture above is displaying 08:50. The hours are represented by the red 1x1,
blue 2x2, and blue 5x5 squares (1+2+5=8). The minutes are represented by the blue 2x2, the
green 3x3, and the blue 5x5 squares (2+3+5=10 and 10*5=50).
The example at the left which uses the inputted characters R, W, G, B, G displays the time 04:50.
The hours are represented by the 1x1 red square and the 3x3 blue square: 1+3=4. The minutes
are represented by the 2x2 green, the 3x3 blue, and the 5x5 green squares: (2+3+5)*5 = 50. The
example at the right which uses the inputted characters W, B, B, G, R displays the time 08:30.
The hours are 1+2+5=8 and the minutes are (1+2+3)*5=30.

2021-2022 ● Contest 1: Fibonacci Clock ● Junior Division

INPUT: There are 5 sets of data. Each set has 5 uppercase letters (R, G, B, or W) that represent
the colors of the lower 1x1, the upper 1x1, the 2x2, the 3x3, and finally the 5x5 square, in that
order. We guarantee that the input will represent a valid time from 00:00 to 11:55.

OUTPUT: For each line of data, print the time in hours and minutes formatted as hh:mm.

SAMPLE INPUT: SAMPLE OUTPUT:
R W G B G 1. 04:50
W B B G R 2. 08:30
B G B B R 3. 11:35
W W W B B 4. 08:40
W R G G G 5. 01:50
'''


class Solution:
    def clock_reader(self, colors: str) -> str:
        fib = [1, 1, 2, 3, 5]
        # Parse the colors
        r = 0
        g = 0
        b = 0
        for i in range(len(colors)):
            if colors[i] == "R":
                r += fib[i]
            elif colors[i] == "G":
                g += fib[i]
            elif colors[i] == "B":
                b += fib[i]
        # calc hours and mins separately
        h = r + b
        m = (g + b) * 5
        # assemble and return
        return f"{h:02}:{m:02}"


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    tests = [("RWGBG", "04:50"),
             ("WBBGR",),
             ("BGBBR",),
             ("WWWBB",),
             ("WRGGG",),
             ("GRWBB",),
             ("RBBWG",),
             ("WWWWW",),
             ("BWWGR",),
             ("WBBBB"),
             ]
    answer = sol.clock_reader("")
    print(answer)
