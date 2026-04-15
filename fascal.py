"""
PROBLEM: One of the many patterns that can be found in Pascal’s Triangle is where the
Fibonacci sequence 1, 1, 2, 3, 5, 8, 13, 21, 34, ... can be found by adding the numbers on the
diagonals as illustrated with the following diagram:

In this program, generate each row of Pascal’s Triangle by placing a 1 in the first and last
position. For the positions in the middle of the triangle, every number is the sum of the numbers
immediately above it. The 0th row contains a single 1. For row N, there are N+1 items.
INPUT: There are 5 lines of data. Each line has a single integer representing one of the
Fibonacci numbers in the following sequence: 1 1 2 3 5 8 13 21 34 55 89 .... We guarantee it
will be less than 1,000,000.
OUTPUT: For each line of data, print the integers on the diagonal of Pascal’s Triangle that add
up to the given number, in the order that they appear in the triangle from bottom left to upper
right separated by a single space.
SAMPLE INPUT:
8
89
610
10946
317811

2021-2022 ● Contest 3: Fibonacci & Pascal ● Junior Division
SAMPLE OUTPUT:
1. 1 4 3
2. 1 9 28 35 15 1
3. 1 13 66 165 210 126 28 1
4. 1 19 153 680 1820 3003 3003 1716 495 55 1
5. 1 26 300 2024 8855 26334 54264 77520 75582 48620 19448 4368
455 14

2021-2022 ● Contest 3: Fibonacci & Pascal ● Junior Division

TEST DATA

TEST INPUT:
2
55
1597
17711
832040

TEST OUTPUT:
1. 1 1
2. 1 8 21 20 5
3. 1 15 91 286 495 462 210 36 1
4. 1 20 171 816 2380 4368 5005 3432 1287 220 11
5. 1 28 351 2600 12650 42504 100947 170544 203490 167960 92378
31824 6188 560 15
"""


class Solution:
    def generate(self, numRows: int):
        if numRows == 1:
            # basecase/housemouse
            return [[1]]
        #             smallercase
        triangle = self.generate(numRows - 1)
        previous = triangle[-1]
        current = [1] * (len(previous) + 1)
        for i in range(1, len(current) - 1):
            current[i] = previous[i - 1] + previous[i]
        triangle.append(current)
        return triangle

    def fetchfibo(self, fibo):
        # 1. get indexx from fibo
        # 2. generate pacal tringal of height = indexx + 1
        #3. do the triangle thing and fat- extracte the triange and return and wait extracte the triange
        pass

    def fascalSolver(self, lst):
        # 1. loop thru lst for each element call snatch pascal
        cont = []
        for fib in lst:
            cont.append(self.fetchfibo(fib))
        return cont


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    tests = [[8,
              89,
              610,
              10946,
              317811
              ]]
    outputs = [[[1, 4, 3],
                [1, 9, 28, 35, 15, 1],
                [1, 13, 66, 165, 210, 126, 28, 1],
                [1, 19, 153, 680, 1820, 3003, 3003, 1716, 495, 55, 1],
                [1, 26, 300, 2024, 8855, 26334, 54264, 77520, 75582, 48620, 19448, 4368, 455, 14]]]
    for i in range(len(tests)):
        lst = tests[i]
        answer = sol.fascalSolver(lst)
        if answer == outputs[i]:
            print("👍👏👍👏👍👏👍👏👍👏👍👏👍👏Yippeee")
            print(answer)
            print(outputs[i])
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
            print(answer)
            print(outputs[i])
