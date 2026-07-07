from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return head
        if not head.next:
            return head
        else:
            new = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return new

#Recursive Solution
#(New -> Just the last element of the linked list)
#The reversal logic is just: head.next.next = head ; head.next = None ('None' required to prevent forming a cycle at the last step)
