class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-2, -1, -1):
        	if nums[i] < nums[i+1]:
        		id = i+1
        		for j in range(i+1,len(nums)):
        			if nums[j] < nums[id]:
        				id = j
        		tmp = nums[i]
        		nums[i] = nums[id]
        		nums[id] = tmp
        		for j in range(i+1, len(nums)):
        			for k in range(i+1, len(nums) - (j-i)):
        				if nums[k] > nums[k+1]:
        					tmp = nums[k]
        					nums[k] = nums[k+1]
        					nums[k+1] = tmp
        		break
        	if i == 1:
            	for j in range(0, len(nums)):
        			for k in range(0, len(nums) - (j+1)):
        				if nums[k] > nums[k+1]:
        					tmp = nums[k]
        					nums[k] = nums[k+1]
        					nums[k+1] = tmp

