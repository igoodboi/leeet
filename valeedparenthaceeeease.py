"""20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            elif c == "]" and stack[-1] == "[":
                stack.pop()
            elif c == ")" and stack[-1] == "(":
                stack.pop()
            elif c == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(c)
        return not stack


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    # [4,3,2,1]
    answer = sol.isValid(s="([{([({})])}])")
    print(answer)
