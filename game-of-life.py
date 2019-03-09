class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)

        if m == 0:
            return

        n = len(board[0])

        # check if cell on board
        def check(x, y):
            return x >= 0 and y >= 0 and x < m and y < n

        hx = [1,1,1,0,0,-1,-1,-1]
        hy = [-1,0,1,-1,1,-1,0,1]
        a = []
        for i in range(m):
            b = []
            for j in range(n):
                val = 0
                for k in range(8):
                    x = i + hx[k]
                    y = j + hy[k]
                    if check(x, y):
                        val += 1
                b.append(val)
            a.append(b)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if a[i][j] < 2:
                        board[i][j] = 0
                    elif a[i][j] <= 3:
                        board[i][j] = 1
                    elif a[i][j] > 3:
                        board[i][j] = 0
                else:
                    if a[i][j] == 3:
                        board[i][j] = 1