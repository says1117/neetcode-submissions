# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
1. check if root, return false if no node.
2. get node, traverse that side. DFS down left first
    2.1 left is null and right is null, pop up from stack returning
        needs to be if not left and if not right, because if we only check 1, then we pop back up without checking the opposite side recursively
            example: there is no left node but there is right. if we check for only 1 side, the other one will not get recursively checked
    2.2 check if theres a left, and if key.val > key.left.val
        if it is, traverse that side
        if it is not, return false
    2.3 check if theres a right and if key.val < key.right.val
        if it is, traverse that side
        if it is not, return false


    new notes:
        pass in upper and lower bounds,
        when u go left, lower bound changes and upper bound same
        when u go right, upper bound changes and lower bound same
3. return True

'''
from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root, upper, lower) -> bool:
            if not (lower < root.val < upper):
                return False
            
            if root.left:
                if root.val > root.left.val:
                    if not dfs(root.left, root.val, lower):
                        return False
                else:
                    return False
            
            if root.right:
                if root.val < root.right.val:
                    if not dfs(root.right, upper, root.val):
                        return False
                else:
                    return False
            
            return True

        return dfs(root, float('inf'), float('-inf'))