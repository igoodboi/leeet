"""
PROBLEM: Given 3 lists of numbers, possibly of different lengths, find the largest number in each
position. For example, In the following 3 lists, the largest number is in bold:
6, 8, 1, 5, 2, 3, 5, 3, 7, 9
7, 6, 2, 9
9, 3, 4, 6, 1, 8, 6, 4, 2, 8, 4
Print the sum of the largest numbers. In the above example: 9 + 8 + 4 + 9 + 2 + 8 + 6 + 4 + 7 + 9 + 4 = 70
INPUT: There will be 5 sets of input data. Each set will have 3 lines containing space-separated
integers.
OUTPUT: Print the sum of the largest number found in each position in the lists.
SAMPLE INPUT: SAMPLE OUTPUT:
6 8 1 5 2 3 5 3 7 9 1. 70
7 6 2 9
9 3 4 6 1 8 6 4 2 8 4
1 3 5 7 9 2 4 6 8 10 2. 101
5 2 6 4 8 7 9 11 14 12
4 2 6 4 7 1 9 22 21 9
5 6 7 8 9 1 2 3. 63
9 8 7 6 5 0 1 2 3 4
8 6 4 2 1 3 5 7
1 4. 6
1 2
1 2 3
31 41 59 26 53 58 97 93 23 84 62 64 33 83 27 5. 1139
56 89 23 14 26 37 48 59 61 72 83 94
42 35 68 79 82 91 20 51 64 97 86

2020-2021 ● Contest 3: Multiple Arrays ● Junior Division

TEST INPUT:
3 1 4 1 5 9 2 6 5 3 5 8 9 7
9 3 2 3 8 4 6 2 7 9 8 5 3 5 6 2 9 5 1 4 1 3
6 2 8 3 1 8 5 3 0 6
31 41 59 26 53 58 97 93 23 84 62 64 33 83 27
21 32 43 54 65 76 87 98 90 70 50 30 10
20 40 60 80 12 23 34 45 56 67 78 89
8765 4321 9012 3456 7890 321 654 987
9123 5326 8975 345 789
7654 6235 5798 6543 4567 32 54 1024 2048 4096
-5 -6 -7 -8 -9 -10 -11
-1 -2 -3 -4 -12 -8 -10 -16 -14 -12 -10 -5
-6 -9 -1 -2 -10 -7 -9 -21 -15 -10
1
1
1
TEST OUTPUT:
1. 131
2. 1032
3. 46946
4. -86
5. 1
"""


class Solution:
    def largeFinderer(self, lst):
        max_length = max([len(l) for l in lst])
        max3 = []
        for i in range(max_length):
            col = []
            for j in range(3):
                if i < len(lst[j]):
                    col.append(lst[j][i])
            max3.append(max(col))
        return sum(max3)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    tests = [((3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7),
              (9, 3, 2, 3, 8, 4, 6, 2, 7, 9, 8, 5, 3, 5, 6, 2, 9, 5, 1, 4, 1, 3),
              (6, 2, 8, 3, 1, 8, 5, 3, 0, 6)),
             ((31, 41, 59, 26, 53, 58, 97, 93, 23, 84, 62, 64, 33, 83, 27),
              (21, 32, 43, 54, 65, 76, 87, 98, 90, 70, 50, 30, 10),
              (20, 40, 60, 80, 12, 23, 34, 45, 56, 67, 78, 89)),
             ((8765, 4321, 9012, 3456, 7890, 321, 654, 987),
              (9123, 5326, 8975, 345, 789),
              (7654, 6235, 5798, 6543, 4567, 32, 54, 1024, 2048, 4096)),
             ((-5, -6, -7, -8, -9, -10, -11),
              (-1, -2, -3, -4, -12, -8, -10, -16, -14, -12, -10, -5),
              (-6, -9, -1, -2, -10, -7, -9, -21, -15, -10)),
             ((1,),
              (1,),
              (1,))]
    outputs = [(131),
               (1032),
               (46946),
               (-86),
               (1)]
    for i in range(len(tests)):
        lst = tests[i]
        answer = sol.largeFinderer(lst)
        if answer == outputs[i]:
            print("👍👏👍👏👍👏👍👏👍👏👍👏👍👏Yippeee")
            print(answer)
            print(outputs[i])
        elif answer != outputs[i]:
            print("BOOOOOOOOOOOOO >:( 🤮😱🤮😱🤮😱🤮😱🤮😱🤮😱")
            print(answer)
            print(outputs[i])
