# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leftBranch(self, root):
        res = []
        while root != None:
            

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        s = []
        res = []
        while True:
            if len(s) == 0:
                u = root
                while u != None:
                    s.append(u)
                    res.append(u.val)
                    u = u.left
                continue
            else:
                u = s.pop()
            print(len(s))
            v = u.right
            if v != None:
                while v != None:
                    s.append(v)
                    res.append(v.val)
                    v = v.left
            if len(s) == 0:
                break
        return res