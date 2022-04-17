# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        cur = last = head
        prev = None
        # print(cur == head)
        # print(head)
        while cur.next is not None:
            # print(f'head:{head.val},cur:{cur.val},prev:{prev.val},last:{last.val}')
            if cur.val == cur.next.val:
                while last is not None and cur.val == last.val:
                    last = last.next
                if cur == head:
                    # print('head changed')
                    head = last
                else:
                    # print('prev changed')
                    prev.next = last
                cur = last

            else:
                prev = cur
                cur = cur.next
                last = cur

            if cur is None:
                break

        return head

