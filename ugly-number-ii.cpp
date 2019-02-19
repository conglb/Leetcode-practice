
class Solution {
public:
	long long binarySearch(vector<long long>& arr, int mul) {
		int val = arr[arr.size()-1];
		int l = 0;
		int r = arr.size() - 1;
		long long res = arr[l] * mul;
		while (l <= r) {
			int m = (l + r) / 2;
			if (arr[m] * mul > val) {
				res = arr[m] * mul;
				r = m - 1;
			}
			else {
				l = m + 1;
			}
		}
		return res;
	} 
    int nthUglyNumber(int n) {
    	vector<long long> arr;
 		arr.push_back(1);
 		long long next = 1;
 		for (int i=2; i<=n; i++) {
 			next = binarySearch(arr, 2);
 			next = min(next, binarySearch(arr, 3));
 			next = min(next, binarySearch(arr, 5));
 			arr.push_back(next);
 		}    	   
 		return next;
    }
};