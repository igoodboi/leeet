"""67. Add Binary
Given two binary strings a and b, return their sum as a binary string.
Example 1:
Input: a = "11", b = "1"
Output: "100"
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
Constraints:
1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(b) > len(a):
            c = len(b) - len(a)
            a = '0' * c + a
        elif len(a) > len(b):
            c = len(a) - len(b)
            b = '0' * c + b
        carry = 0
        result = []
        for i in range(len(a), 0,-1):
            da = int(a[i-1])
            db = int(b[i-1])
            tot = da + db + carry
            carry = tot // 2
            result.append(str(tot % 2))
        if carry == 1:
            result.append(str(1))
        return ''.join(result[::-1])

    def addBinary1(self, a: str, b: str) -> str:
        num1 = int(a, 2)
        num2 = int(b, 2)
        sumthin = num1 + num2
        binary_sum = bin(sumthin)
        return binary_sum[2:]


if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)
    sol = Solution()
    answer1 = sol.addBinary(a="10101010101010101001", b="101010101110101")
    answer2 = sol.addBinary1(a="10101010101010101001", b="101010101110101")
    print(answer2,answer1)
