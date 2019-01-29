class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        s = '  ' + s
        n = len(s)
        ans = ''
        for i in range(2,numRows+2):
            tmp = i
            if i < n:
                if i != numRows+1:
                    ans += s[i]
            else:
                break
            tmp = 2
            while True:
                tmp += 2 * (numRows) - 2
                if tmp - (i-2) < n:
                    ans += s[tmp - i + 2]
                else:
                    break
                if i != 2 and i != numRows+1:
                    if tmp + (i-2) < n:
                        ans += s[tmp + i - 2]
                    else:
                        break
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.convert('PAYPALISHIRING',4))

