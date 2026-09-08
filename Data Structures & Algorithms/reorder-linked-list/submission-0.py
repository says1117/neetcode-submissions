# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        t = head
        node = []
        while t:
            node.append(t)
            t = t.next

        # starts at 0 and 4 indexes
        i, j = 0, len(node)-1
        while i < j:
            node[i].next = node[j]
            i += 1
            #possibility to break after i is incremented
            if i >= j:
                break
            node[j].next = node[i]
            j-=1

        #terminate the list
        node[i].next = None
