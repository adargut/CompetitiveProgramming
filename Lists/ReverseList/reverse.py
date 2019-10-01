# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None

        prev, cur, nxt = None, head, head.next

        while cur.next:
            cur.next = prev
            prev = cur
            cur = nxt
            nxt = cur.next
        cur.next = prev
        head = cur

        return head