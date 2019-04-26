class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(int(min(n,m)/2) + 1):
            mm = m - i - 1
            nn = n - i - 1
            if i > mm or i > nn:
                break
            # i <= mm and i <= nn
            # above
            for j in range(i, nn + 1):
                res.append(matrix[i][j])
            # right
            for j in range(i + 1, mm + 1):
                res.append(matrix[j][nn])
            if i < mm:
                for j in range(nn-1, i-1, -1):
                    res.append(matrix[mm][j])
            if i < nn:
                for j in range(mm-1, i, -1):
                    res.append(matrix[j][i])

        return res