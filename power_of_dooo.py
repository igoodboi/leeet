"""
231. Power of Two
Easy
Topics
Companies
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-2^31 <= n <= 2^31 - 1
 

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        if n & (n - 1) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.isPowerOfTwo(n=1)
    print(answer)
