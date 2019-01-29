# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def caculateBalancedIndex(self, root):
        if root == None:
            return 0
        res = 0
        res = self.caculateBalancedIndex(root.left) + 1
        res = max(res, self.caculateBalancedIndex(root.right) + 1)
        return res

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return abs(self.caculateBalancedIndex(root.left) - self.caculateBalancedIndex(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

