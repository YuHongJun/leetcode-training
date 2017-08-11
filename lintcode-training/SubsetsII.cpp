#include<vector>
#include<algorithm>
using namespace std;


class Solution {
public:
    vector<vector<int> > result;
    bool equls( vector<int> a, vector<int> b){
        if (a.size() != b.size())
            return false;
        int cnt = a.size();
        for (int i = 0; i < cnt;++i)
            if (a[i]!=b[i]) return false;
        return true;
    }
    void dfs(vector<int> tmp, int x , vector<int> nums) {
        if (x == nums.size()) {
            int cnt = result.size();
            for ( int i = 0; i  < cnt ; ++i)
                if ( equls(result[i], tmp) )
                        return ;
            result.push_back(tmp);
            return ;
        }
        dfs(tmp, x + 1, nums);
        tmp.push_back(nums[x]);
        dfs(tmp, x + 1, nums);
    }
    vector<vector<int> > subsetsWithDup(vector<int> &nums){
        sort(nums.begin(), nums.end());
    	vector<int> tmp;
    	dfs(tmp, 0 , nums) ;
    	// write your code here
    	return result;
    }
};

//int main(){
//    Solution result;
//
//    result.subsetsWithDup([1, 2, 2]);
//}