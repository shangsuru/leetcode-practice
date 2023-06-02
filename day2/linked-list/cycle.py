from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        
        tortoise = head
        hare = head.next

        while True:
            if tortoise == hare:
                return True

            if hare.next == None or hare.next.next == None:
                return False
            
            tortoise = tortoise.next
            hare = hare.next.next
            