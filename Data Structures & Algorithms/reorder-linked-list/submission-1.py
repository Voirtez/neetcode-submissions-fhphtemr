# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        front = head
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        current = slow.next
        slow.next = None
        prv = None
        
        while current:
            nxt = current.next
            current.next = prv
            prv = current
            current = nxt
        
        back = prv

        while front and back:
            f_nxt = front.next
            b_nxt = back.next
            front.next = back
            back.next = f_nxt
            front = f_nxt
            back = b_nxt

            
            


        