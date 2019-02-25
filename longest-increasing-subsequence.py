class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for num in nums:

            # find in arr
            def binarySearch():
                l = 0
                r = len(arr) - 1
                res = -1
                while l <= r:
                    m = int((l + r) / 2)
                    if arr[m] >= num:
                        res = m
                        r = m - 1
                    else:
                        l = m + 1
                return res

            tmp = binarySearch()

            # three case
            if tmp == -1:
                arr.append(num)
            else:
                if arr[tmp] >= num:
                    arr[tmp] = num

        return len(arr)

