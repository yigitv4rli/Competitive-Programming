# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inOrder(root):
            if root == None:
                return []
            else:
                return inOrder(root.left) + [root.val] + inOrder(root.right)
            
        return sorted(inOrder(root))[k-1]
        
        
        
        
