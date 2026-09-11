# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        t = head
        count = 0
        while t:
            count+=1
            t = t.next
        res = head
        c = 0
        if count-n == 0:
            return res.next
        while (count - n) >= c and head:
            c+=1
            if c == (count-n):
                if head.next:
                    temp = head.next.next
                    head.next = temp
                else:
                    head.next = None
                break
            head = head.next
        return res