class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort(key=lambda element: element[0])
        for i in range(len(a) - 1):
            j = i+1
            while j < len(a):
                if a[j][0] > a[i][1]:
                    j += 1
                else:
                    a[i][1] = max(a[j][1], a[i][1])
                    del a[j]
        return a
