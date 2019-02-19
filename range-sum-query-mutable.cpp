#include <bits/stdc++.h>

using namespace std;


class IntervalTree {
    public:
        IntervalTree() {
            cout <<"init it" << endl;
        }
        void update(int i, int l, int r, int x, int val) {
            if (l > x || r < x) return;
            if (l == r) {
                t[i] += val;
                return;
            }
            t[i] += val;
            int m = (l + r) / 2;
            update(i*2,l,m,x,val);
            update(i*2+1,m+1,r,x,val);
        }
        int get(int i, int l, int r, int ll, int rr) {
            // no intersection area case
            if (ll > r || rr < l) {
                return 0;
            }
            if (ll <= l && r <= rr) {
                return t[i];
            }
            int m = (l + r) / 2;
            int s1 = get(i*2,l,m,ll,rr);
            int s2 = get(i*2+1,m+1,r,ll,rr);
            cout << l << " " << r  << " " << s1+s2<< endl;
            return s1+s2;
        }
    private:
        int t[100000*4];
};



class NumArray {
public:
    NumArray(vector<int> nums) {
        it = new IntervalTree();
        n = nums.size();
        for (int i=0; i<nums.size(); i++) {
            cout << i << endl;
            it->update(1,1,n,i+1, nums[i]);
        }
    }

    ~NumArray() {
        delete it;
    }
    
    void update(int i, int val) {
        int oldVal = it->get(1,1,n,i+1,i+1);
        int gap =  oldVal - val;
        it->update(1,1,n,i+1,val); 
    }
    
    int sumRange(int i, int j) {
        cout << "get" << endl;
        return it->get(1,1,n,i+1,j+1);
    }
private:
    int n;
    IntervalTree* it;
};

int main() {
    vector<int> v;
    v.push_back(1);
    v.push_back(2);
    v.push_back(2);
    NumArray* a = new NumArray(v);
    cout << a->sumRange(0,0);
    return 0;
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(i,val);
 * int param_2 = obj.sumRange(i,j);
 */