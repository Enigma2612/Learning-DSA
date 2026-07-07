from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (not list1) and list2:
            return list2
        if (not list2) and list1:
            return list1
        
        p1, p2 = None, None
        h = None
        while list1 and list2:
            if list1.val < list2.val:
                if p1 == p2 == None:
                    h = list1
                temp = list1.next
                if p2:
                    p2.next = list1
                list1.next = list2
                p2 = list1
                list1 = temp
                p1 = None

            else:
                if p1 == p2 == None:
                    h = list2
                temp = list2.next
                list2.next = list1
                if p1:
                    p1.next = list2
                p1 = list2
                list2 = temp
                p2 = None

        return h