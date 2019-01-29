class Solution:
    def caculate(self, str):
        char = list(str)
        char.sort()
        return tuple(char)
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tup = []
        for str in strs:
            tup.append(self.caculate(str))
        d = {}
        for i in range(len(strs)):
            d[tup[i]] = list()
        for i in range(len(strs)):
            d[tup[i]].append(strs[i])
        return list(d.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))