'''
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = str(x)
        for i in range(len(y) // 2):
            if y[-i - 1] != y[i]:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    # 121 = true
    # -121 = false
    # 10 = false
    n = 11111111111112222222222221111111111111
    answer = sol.isPalindrome(n)
    print(answer)
