class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if head is None:
            return
        
        ll = []
        while head is not None:
            ll.append(head)
            head = head.next
        
        newHead = Node(ll[0].val, None, None)
        cur = newHead
        ll2 = [newHead]
        for i in range(1,len(ll)):
            node = Node(ll[i].val, None, None)
            cur.next = node
            ll2.append(node)
            cur = node
        # ll2.append(Node(None,None,None))
        
        for i, item in enumerate(ll):
            num = search (ll, item.random)
            # print(num, ll2)
            if num < len(ll):
                ll2[i].random = ll2[num]
        
        return newHead

def search(ll, node):
    for i, item in enumerate(ll):
        if node is item:
            return i
    return len(ll)