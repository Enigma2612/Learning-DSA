# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return None
        lis1 = h1 = ListNode()
        lis2 = h2 = ListNode()

        while head:
            h1.next = ListNode()
            h1.next.val = head.val
            h2.next = ListNode()
            h2.next.val = head.val
            head = head.next
            h1 = h1.next
            h2 = h2.next
        
        lis1 = lis1.next
        lis2 = lis2.next

        dummy = node = ListNode()

        prev = None
        n = 0

        while lis2:
            temp = lis2.next
            lis2.next = prev
            prev = lis2
            lis2 = temp
            n += 1
            
        lis2 = prev
        count = n


        while count:
            count -= 1
            if (n-count)%2:
                dummy.next = lis1
                lis1 = lis1.next
            else:
                dummy.next = lis2
                lis2 = lis2.next
            dummy = dummy.next
        
        return node.next


#node.next is the required output, but not what the question wants
#The question wants in-place modification
#Still this was a straight forward way I thought I'd keep noted down