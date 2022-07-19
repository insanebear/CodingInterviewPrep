class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll = []
        while head is not None:
            ll.append(head.val)
            head = head.next
        # ll.append(head.val)
        ll.sort()
        
        head = ListNode()
        if len(ll) == 0:
            return 
        head.val = ll[0]
        cur = head
        for i in range(1,len(ll)):
            node = ListNode()
            node.val = ll[i]
            cur.next = node
            cur = node
        return head