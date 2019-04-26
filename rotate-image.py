class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(a)
        for i in range(int(n / 2)):
            m = n - i - 1
            for j in range(i, n - i-1):
                # left-top
                tmp = a[i][j] 
                a[i][j] = a[m - (j-i)][i]
                # top-right
                tmp, a[j][m] = a[j][m], tmp
                # right-bottom
                tmp, a[m][m - (j-i)] = a[m][m- (j-i)], tmp
                # bottom-left
                tmp, a[m - (j-i)][i] = a[m - (j-i)][i], tmp~