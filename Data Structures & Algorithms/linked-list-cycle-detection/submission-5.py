# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        d = {}

        while head:
            if head is None:
                break
            if head.val not in d:
                d[head.val] = 0
            else:
                d[head.val] +=1
                if d[head.val] > 1:
                    return True


            head = head.next

        return False