class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(len(nums)-1):
            nums.append(nums[i])
        s = []
        res = []
        for i in range(len(nums)-1, -1, -1):
            while len(s) > 0 and s[len(s)-1] <= nums[i]:
                s.pop()
            if i < n:
                if len(s) > 0:
                    res.append(s[len(s)-1])
                else:
                    res.append(-1)
            s.append(nums[i])
        res.reverse()
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.nextGreaterElements([1,2,1]))
