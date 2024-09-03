str = ''.join(list)
if __name__ == '__main__':
    import sys

    sys.setrecursionlimit(1501)


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

