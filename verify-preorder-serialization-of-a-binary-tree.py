class Solution:
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder = preorder.split(',')
        if preorder.pop() != '#':
            return False
        s = []
        for char in preorder:
            if char == '#':
                if len(s) > 0:
                    s.pop()
                else:
                    return False
            else:
                s.append(char)
        return True
