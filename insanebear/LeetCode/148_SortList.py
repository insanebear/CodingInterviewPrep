# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find a tail
        node = head
        tail = None
        count = 0
        while node != None:
            if node.next == None:
                tail = node
            node = node.next
            count += 1
            
        # merge sort
        def mergeSort(left, right, count):
            # base
            if left is right:
                return left
            
            # find a mid
            m_count = count//2
            mid = left
            
            for _ in range(1, m_count): # move mid as much as m_count
                mid = mid.next

            # -- divide [left new_right] [new_left right]
            new_right = mid
            new_left = mid.next
            mid.next = None
            
            leftList = mergeSort(left, new_right, m_count)
            rightList = mergeSort(new_left, right, count - m_count)
            
            # -- merge sort
            p1 = leftList
            p2 = rightList
            
            # set head
            new_head = None
            new_tail = None
            if leftList.val < rightList.val:
                new_head = leftList
                new_tail = leftList
                p1 = leftList.next
            else:
                new_head = rightList
                new_tail = rightList
                p2 = rightList.next
                
            # sort
            while (p1 is not None) and (p2 is not None):
                if p2.val < p1.val:
                    new_tail.next = p2
                    p2 = p2.next
                    new_tail = new_tail.next
                else:
                    new_tail.next = p1
                    p1 = p1.next
                    new_tail = new_tail.next
            
            if p1 is None:
                new_tail.next = p2
                p2 = p2.next
                new_tail = new_tail.next
                    
            elif p2 is None:
                new_tail.next = p1
                p1 = p1.next
                new_tail = new_tail.next
            
            return new_head
            
        return mergeSort(head, tail, count)