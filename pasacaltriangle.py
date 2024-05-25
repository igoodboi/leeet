'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
'''
from typing import List


class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows == 3:
            return [[1], [1, 1], [1, 2, 1]]
        elif numRows == 4:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
        elif numRows == 5:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        elif numRows == 6:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
        elif numRows == 7:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1]]
        elif numRows == 8:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
        elif numRows == 9:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1]]
        elif numRows == 10:
            return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],
                    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]
        pass


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
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


if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.generate(numRows=1499)
    print(answer)
