class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # number of rows
        m = len(matrix)
        # matrix = [] case
        if m == 0:
            return 0

        # number of collums
        n = len(matrix[0])
        mark = []
        for _ in range(m):
            mark.append([-1] * n)

        hx = [1,-1,0,0]
        hy = [0,0,-1,1]

        global ans, arrans
        ans = 0
        arrans = []
        topo = []

        def DFS(u, v):
            global ans, arrans
            if mark[u][v] != -1:
                return mark[u][v]
            def checkOnBoard(x,y):
                return x < m and y < n and x > -1 and y > -1
            res = 1
            for i in range(4):
                x = u + hx[i]
                y = v + hy[i]
                if checkOnBoard(x, y) and matrix[x][y] > matrix[u][v]:
                    res = max(res, DFS(x,y) + 1)
            mark[u][v] = res
            topo.append(matrix[u][v])
            if res > ans:
                ans = res
                arrans = topo[:]
            return res

        for u in range(m):
            for v in range(n):
                if mark[u][v] == -1:
                    topo = []
                    DFS(u,v)

        return(ans)

