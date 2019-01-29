class Solution:

    def update(self):
        # check
        for i in range(self.n):
            for j in range(i+1,self.n):
                # prime
                if i - self.x[i] == j - self.x[j]:
                    return
                # extra
                if i + self.x[i] == j + self.x[j]:
                    return
                if self.x[i] == self.x[j]:
                    return
        m = []
        for i in range(self.n-1,-1,-1):
            s = self.x[i] * '.' + 'Q' + (self.n-self.x[i]-1) * '.'
            m.append(s)
        self.res.append(m)
    def attempt(self , i):
        for j in range(self.n):
            if self.mark[j] == False:
                self.x.append(j)
                self.mark[j] = True
                if i == self.n-1:
                    self.update()
                else:
                    self.attempt(i+1)
                self.mark[j] = False
                self.x.pop()

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.x = []
        self.mark = [False] * n
        self.res = []
        self.attempt(0)
        return self.res

if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))