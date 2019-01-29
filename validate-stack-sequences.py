class Solution:
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        popped.reverse()
        pushed.reverse()
        stack = []
        while len(popped) > 0 and (len(pushed) > 0 or (len(stack) > 0 and stack[len(stack)-1] == popped[len(popped)-1])):
            if len(stack) > 0 and stack[len(stack)-1] == popped[len(popped)-1]:
                stack.pop()
                popped.pop()
            else:
                stack.append(pushed.pop())
        if len(popped) == 0 :
            return True
        else:
            return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.validateStackSequences([1,2,3,4,5],[4,5,3,2,1]))