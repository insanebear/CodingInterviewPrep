# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        node = head
        prev = ListNode(next = head)
        while node and node.next:
            if node.val == node.next.val:
                new_node = node.next.next
                while new_node and node.val == new_node.val:
                    new_node = new_node.next
                prev.next = new_node
                node = new_node
            else:
                prev = node
                node = node.next
        
        while head and head.next and head.val == head.next.val:
            new_node = head.next.next
            while new_node and head.val == new_node.val:
                new_node = new_node.next
            head = new_node
            
        return head