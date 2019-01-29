class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pos = {}
        ans = 0
        j = 0
        for i in range(len(s)):
            if s[i] in pos.keys():
                j = pos[s[i]] + 1
                pos[s[i]] = i
            else:
                pos[s[i]] = i
            print (i, j)
            ans = max(ans, i - j + 1)
        return ans

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring('abba'))