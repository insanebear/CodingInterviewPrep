# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead=ListNode(0, head)
        n = newHead
                
        while head:
            if head.next != None and head.val == head.next.val:
                while head.next != None  and head.val == head.next.val:
                    head = head.next
                    
                n.next = head.next
            else:
                n = n.next
            head = head.next
        
        return newHead.next