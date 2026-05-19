# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        current = None
        carry = 0

        while l1 or l2 or carry == 1:
            if not l1:
                l1_val = 0
            else:
                l1_val = l1.val
                l1 = l1.next
            
            if not l2:
                l2_val = 0
            else:
                l2_val = l2.val
                l2 = l2.next
            
            current_val = l1_val + l2_val + carry

            if current_val >= 10:
                current_val -= 10
                carry = 1
            else:
                carry = 0

            if current is None:
                current = ListNode(current_val)
                head = current
            else:
                current.next  = ListNode(current_val)
                current = current.next

        return head