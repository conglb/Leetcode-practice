class Solution:
    def update(self):
        s = [i for i in self.s]
        self.res.append(s)
    def attempt(self, i):
        if i == self.n:
            self.update()
            return
        for j in self.d.keys():
            if self.d[j] > 0:
                self.s.append(j)
                self.d[j] -= 1
                self.attempt(i+1)
                self.d[j] += 1
                self.s.pop()
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # init
        self.s = []
        self.res = []
        self.d = {}
        self.n = len(nums)
        for i in range(self.n):
            self.d[nums[i]] = 0
        for i in range(self.n):
            self.d[nums[i]] += 1

        self.attempt(0)

        return self.res

if __name__ == '__main__':
    sol = Solution()
    print(sol.permuteUnique([1,2,1]))


