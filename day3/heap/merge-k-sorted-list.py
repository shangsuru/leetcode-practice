from typing import List, Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []
        for lst in lists:
            while lst:
                vals.append(lst.val)
                lst = lst.next
        
        vals = sorted(vals, reverse=True)

        final = None
        for val in vals:
            final = ListNode(val, final)

        return final
