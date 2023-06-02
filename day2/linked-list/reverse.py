from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.next == None:
            return head

        p1 = head
        p2 = head.next
        p3 = head.next.next

        head.next = None

        while True:
            p2.next = p1

            if p3 == None:
                break

            p1 = p2
            p2 = p3
            p3 = p3.next
        
        return p2
            

