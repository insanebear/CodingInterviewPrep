"""
<https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/>
"""

from types import Optional, 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - Remove duplicated items
        """
        prev = None
        first = head
        last = head
        head = None
        
        while last:
            while last and first.val == last.val:
                last = last.next

            if first.next is last:
                # current: unique
                if prev is None:
                    prev = first
                    head = prev
                else:
                    prev.next = first
                    prev = first

            first = last
            
        if prev:
            prev.next = last
            
        return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        - Use auxiliary memory: make new nodes by copying the unique values
        """
        fast = head
        slow = None
        unique_list = None
        
        while fast:
            if fast.next and fast.val == fast.next.val:
                skip = fast.val
                while fast and fast.val == skip:
                    fast = fast.next
            else:
                if slow is None:
                    unique_list = ListNode(val=fast.val)
                    slow = unique_list
                else:
                    slow.next = ListNode(val=fast.val)
                    slow = slow.next
                fast = fast.next        
        
        return unique_list
        
        