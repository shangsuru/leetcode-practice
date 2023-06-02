from typing import List, Optional
from heapq import heapify, heappop, heappush

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

     def __lt__(self, other):
        return self.val < other.val

class Solution:   
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heads = []
        sortedList = ListNode()
        root = sortedList
                
        for l in lists:
            if l:
                heads.push(l.val, l)
            
        heapify(heads)
        
        while heads:
            smallestElement = heappop(heads)
            
            sortedList.next = smallestElement[1]
            sortedList = sortedList.next
            
            if smallestElement[1].next:
                heappush(heads, (smallestElement[1].next.val, smallestElement[1].next))                   
        
        return root.next