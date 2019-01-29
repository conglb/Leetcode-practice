class Solution:
    def update(self):
        self.res.append([])
        for i in range(self.n):
            self.res[len(self.res)-1].append(self.s[i])
    def attempt(self, i):
        if i == self.n:
            self.update()
            return
        for j in range(self.n):
            if self.mark[j] == False:
                self.mark[j] = True
                self.s.append(self.a[j])
                self.attempt(i+1)
                self.mark[j] = False
                self.s.pop()

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.a = nums
        self.res = []
        self.s = []
        self.n = len(nums)
        self.mark = [False for i in range(self.n)]
        self.attempt(0)
        return self.res

if __name__ =="__main__":
    sol = Solution()
    print(sol.permute([1,2,3]))
