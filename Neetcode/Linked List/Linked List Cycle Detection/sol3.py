from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == 'seen':
                return True
            head.val = 'seen'
            head = head.next
        
        return False

#Found this solution online in a YT comment section
#Super easy and very intuitive solution
#O(n) time, O(1) space