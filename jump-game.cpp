class Solution {
public:
    bool canJump(vector<int>& nums) {
        deque<int> q;
        q.push_back(0);
        int n = nums.size() - 1;
        for (int i=0; i<=n; i++) {
            while (!q.empty() && q.front() < i) q.pop_front();
            if (q.empty()) {
                return false;
            }
            int cur = min(i + nums[i], n);
            if (cur == n) {
                return true;
            }
            while (!q.empty() && q.back() <  cur) q.pop_back();
            q.push_back(cur); 
        }
        return false;
    }
};
