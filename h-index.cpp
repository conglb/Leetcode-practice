class Solution {
public:
    int hIndex(vector<int>& citations) {
        if (citations.size() == 0) return 0;
        sort(citations.begin(), citations.end());
        int remain = 0;
        int res = 0;
        if (citations[0] > citations.size()) res = citations.size();
        for (int i = citations.size() - 1; i >= 0; i--) {
            remain++;
            if (citations[i] <= remain) {
                res = max(res, citations[i]);
            } else {
                res = max(res, remain);
            }
        }
        return res;
    }
};