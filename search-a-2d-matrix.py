class Solution:
    """
    :type a: List[int]
    :type target: int
    :rtype: int
    """
    def binarySearch(self, a, target):
        l = 0;
        r = len(a) - 1;
        res = 0;
        while l <= r:
            m = int((l+r) / 2);
            if a[m] >= target:
                res = m
                r = m-1;
            else:
                l = m+1;
        return res
    
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # check matrix empty case
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        maxline = []
        for line in matrix:
            if len(line) > 0:
                maxline.append(line[len(line)-1]);
        
        lineid = self.binarySearch(maxline, target);
        res = self.binarySearch(matrix[lineid], target);
        
        if matrix[lineid][res] == target:
            return True
        else:
            return False
        
        