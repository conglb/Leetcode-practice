class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                s.append(c)
            else:
                if len(s) == 0:
                    return False
                if c != s.pop():
                    return False
        if len(s) == 0:
            return True
        else:
            return False