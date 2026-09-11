# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        #placing the right node n nodes away from the left
        #doing this will allow us to do a left.next = left.next.next to eliminate our
        #designated value
        while n > 0:
            right = right.next
            n-=1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
