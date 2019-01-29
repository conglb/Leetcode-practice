class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(-112345678)
        i = 0
        j = 0
        while j < len(nums)-1:
            while nums[j] == nums[j+1]:
                j += 1
            nums[i] = nums[j]
            i += 1
            j += 1
        return (i)