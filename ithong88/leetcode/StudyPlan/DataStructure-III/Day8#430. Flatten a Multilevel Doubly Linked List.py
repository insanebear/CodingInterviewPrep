"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        next_list = []

        curr = head
        while curr:
            # When child exists
            while curr.child:
                next_list.append(curr.next)
                curr.next = curr.child
                curr.child.prev = curr
                temp = curr
                curr = curr.child
                temp.child = None

            # when meet end node
            while curr.next is None and len(next_list) > 0:
                next_temp = next_list.pop()
                curr.next = next_temp
                if next_temp:
                    next_temp.prev = curr
                    curr = next_temp

            curr = curr.next

        return head



