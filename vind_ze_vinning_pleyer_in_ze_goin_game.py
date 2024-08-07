'''
3222. Find the Winning Player in Coin Game
Easy
Companies
Hint
You are given two positive integers x and y, denoting the number of coins with values 75 and 10 respectively.

Alice and Bob are playing a game. Each turn, starting with Alice, the player must pick up coins with a total value 115.
If the player is unable to do so, the other player wins the game.

Return the name of the player who wins the game if both players play optimally.



Example 1:

Input: x = 2, y = 7

Output: "Alice"

Explanation:

The game ends in a single turn:

Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.
Example 2:

Input: x = 4, y = 11

Output: "Bob"

Explanation:

The game ends in 2 turns:

Alice picks 1 coin with a value of 75 and 4 coins with a value of 10.
Bob picks 1 coin with a value of 75 and 4 coins with a value of 10.


Constraints:

1 <= x, y <= 100
'''


class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        if x == 0 or y == 0:
            return 'Bob'
        nums_rounds = y // 4
        nums_rounds2pointo = x // 1
        max_stuff = min(nums_rounds,nums_rounds2pointo)
        if max_stuff % 2 == 0:
            return 'Bob'
        else:
            return 'Alice'


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.losingPlayer(x=1, y=8)
    print(answer)
