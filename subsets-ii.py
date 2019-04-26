class Solution:
    """
    [3, 3, 3] => [3, [3, 3], [3, 3, 3]]
    """

    def update(self, state, arr, res, n):
        cur = []
        for i in range(n):
            if state[i] == -1:
                continue

            pattern = arr[i][state[i]]
            for num in pattern:
                cur.append(num)
        res.append(cur)

    def backtrack(self, i, state, arr, res, n):
        for j in range(-1,len(arr[i])):
            state.append(j)
            if i == n-1:
                self.update(state, arr, res, n)
            else:
                self.backtrack(i+1, state, arr, res, n)
            state.pop()
        

    def subsetsWithDup(self, nums):
        # empty list
        if len(nums) < 1:
            return []
        nums.sort()
        # prepare arr
        arr = [[[nums[0]]]]
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                # add new item
                item = []
                for j in range(i,-1,-1):
                    if nums[j] == nums[i]:
                        item.append(nums[j])
                    else:
                        break
                arr[len(arr) - 1].append(item)
            else:
                arr.append([[nums[i]]])

        # backtrack or recurence
        n = len(arr)
        res = []
        state = []
        self.backtrack(0, state, arr, res, n)
        return res

