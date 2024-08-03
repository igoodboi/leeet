'''
70. Climbing Stairs EasyTopicsCompaniesHint You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''


class Solution:

    def __init__(self) -> None:
        self.cache=dict()

    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n < 3:
            return n
        result = self.climbStairs(n - 2) + self.climbStairs(n - 1)
        self.cache[n]=result
        return result


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.climbStairs(n=44)
    print(answer)
