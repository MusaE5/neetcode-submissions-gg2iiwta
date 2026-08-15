class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        if(nums.size() == 1 || nums.size() == 0){
            return nums;
        }

        vector<int> prefix{1};

        int pre = 1;
        for(int i = 1; i<nums.size(); ++i){
            pre *= nums[i-1];
            prefix.push_back(pre);
        }

        vector<int> suffix{1};
        int suff = 1;
        for(int i = nums.size() - 2; i>=0; --i){
            suff *= nums[i+1];
            suffix.push_back(suff);
        }

        // reverse order of suffix
        reverse(suffix.begin(), suffix.end());

        vector<int> result;

        for(int i = 0; i < nums.size(); ++i){
            result.push_back(prefix[i] * suffix[i]);
        }

        return result;

    }
};
