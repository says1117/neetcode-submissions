# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # fast slow pointer method
        fast, slow = head, head

        #fast tracked in the while loop because it will hit fast.next == None fastest
        # if this is hit, then theres no cycle, return False
        # never hits? there is cycle. the loop will hit it eventually

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False