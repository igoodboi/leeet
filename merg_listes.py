"""21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # This class contains the method mergeTwoLists which takes two linked lists (list1 and list2) and returns a merged sorted linked list.
        new_list = ListNode(0)
        thingy = new_list
        while list1 or list2:
            # This while loop continues until both list1 and list2 are exhausted. Inside the loop:
            if list1 is None:
                thingy.next = list2
                list2 = list2.next
            elif list2 is None:
                thingy.next = list1
                list1 = list1.next
            else:
                # this is the mega bosssos
                if list1.val < list2.val:
                    thingy.next = list1
                    list1 = list1.next
                else:
                    thingy.next = list2
                    list2 = list2.next
            thingy = thingy.next
        thingy.next = None
        return new_list.next


if __name__ == '__main__':
    import sys


    def toLinkedList(values):
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
    list1 = [1, 2, 4, 213, 14124, 1423141]
    list2 = [431, 131234, 141241324]
    answer1 = sol.mergeTwoLists(toLinkedList(list1), toLinkedList(list2))
    ans = linkedListToList(answer1)
    print(ans)
