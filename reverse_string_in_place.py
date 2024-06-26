"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.



Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)):
            j = len(s) - 1 - i
            if i >= j:
                break
            tmp = s[i]
            s[i] = s[j]
            s[j] = tmp


if __name__ == '__main__':
    '''
    Input: s = ["h", "e", "l", "l", "o"]
    Output: ["o", "l", "l", "e", "h"]
    Input: s = ["H", "a", "n", "n", "a", "h"]
    Output: ["h", "a", "n", "n", "a", "H"]
    '''

    sol = Solution()
    inpute = ["h", "e", "c"]
    print(inpute)
    sol.reverseString(inpute)
    print(inpute)
