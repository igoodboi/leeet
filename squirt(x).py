"""69. Sqrt(x)
Easy
Topics
Companies
Hint
Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1

"""


class Solution:
    def mySqrt(self, x: int) -> int:
        def binary_search_dingy(m, n):
            if m >= n:
                return n
            y = (m + n) // 2
            y_two_point_o = y * y
            mega_y = (y + 1) * (y + 1)
            if mega_y > x and y_two_point_o <= x:
                # then yippee
                return y
            elif y_two_point_o > x:
                return binary_search_dingy(m, y - 1)
            elif mega_y <= x:
                return binary_search_dingy(y + 1, n)

        return binary_search_dingy(0, x)


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    answer = sol.mySqrt(x=58239578920572398573452)
    print(answer)
