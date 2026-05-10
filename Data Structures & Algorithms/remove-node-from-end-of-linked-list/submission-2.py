# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head or not head.next:
            return None



        total = 0
        curr = head

        while curr:
            total += 1
            curr = curr.next

        if total == n:
            nxt = head.next
            head.next = None
            head = nxt
            return head

        from_front = (total - n)
        curr = head

        i = 1
        while i != from_front:
            curr = curr.next
            i += 1
        
        rm = curr.next

        curr.next = rm.next
        rm.next = None

        return head


        










        