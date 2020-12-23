# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



def helper(r1, r2):
    if not r1 and not r2:
        return True
    if r1 and not r2:
        return False
    if r2 and not r1:
        return False

    return r1.val == r2.val and helper(r1.left,r2.right) and helper(r1.right,r2.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        return helper(root.left,root.right)
