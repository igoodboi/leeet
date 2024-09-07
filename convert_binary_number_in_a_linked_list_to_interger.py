"""1290. Convert Binary Number in a Linked List to Integer
Easy
Topics
Companies
Hint
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        while head:
            result = result << 1
            result = result + head.val
            head = head.next
        return result


if __name__ == '__main__':
    import sys


    def listToLinkedList(values):
        anchor = ListNode(None)
        head = anchor
        for i in values:
            head.next = ListNode(i)
            head = head.next
        return anchor.next


    def linkedListToList(head: ListNode):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result


    sys.setrecursionlimit(1501)
    sol = Solution()
    linked_list = listToLinkedList([1,0,1,0,1])
    answer1 = sol.getDecimalValue(head=linked_list)
    print(answer1)
