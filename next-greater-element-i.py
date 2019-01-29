class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for n1 in nums1:
            overcome = False
            for n2 in nums2:
                if n1 == n2:
                    overcome = True
                if n2 > n1 and overcome:
                    res.append(n2)
                    overcome = False
                    break
            if overcome:
                res.append(-1)
        return res