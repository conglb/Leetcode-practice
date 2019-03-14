class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        k_remain = K
        pos = 1
        res = 0
        for i in range(len(A))
            if i != 0:
                if a[i-1] == 0:
                    k_remain += 1
            if a[i] == 0:
                k_remain -= 1
            while (pos < len(A) and k_remain > 0):
                if a[pos] == 0:
                    k_remain -= 1
                pos += 1
            res = max(res, pos - i)