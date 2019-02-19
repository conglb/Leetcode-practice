class Solution {
public:
	int binarySearch(vector<int>& a) {
		int l = 0;
		int r = a.size() - 1;
        int n = r;
		int res = -1;
		while (l <= r) {
			int m = (l + r) / 2;
			if (a[m] <= n - m + 1) {
				l = m + 1;
				res = m; 
			} else {
				r = m - 1;
			}
		}
		return res;
	}
    int hIndex(vector<int>& citations) {
        if (citations.size() == 0) return 0;
        if (citations.size() == 1) return min(citations[0], 1);
        int n = citations.size() - 1;
        int pos = binarySearch(citations);
        if (pos == -1) {
        	return citations.size();
        }
        int res = citations[pos];
        if (pos < n) {
        	if (citations[pos+1] >= n - pos) {
        		if (res < n - pos) {
                    res = n - pos;
                }
        	}
        }
        return res;
    }
};