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
        self.res += 1
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

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.x = []
        self.mark = [False] * n
        self.res = 0
        self.attempt(0)
        return self.res

if __name__ == "__main__":
    sol = Solution()
    print(print(sol.solveNQueens(4)))