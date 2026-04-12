class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0;
        int minLength = INT_MAX;
        int sum = 0;

        for(int r = 0; r<nums.size();r++){
            if(nums[r] >= target){
                return 1;
            }

            sum += nums[r];

            while(l<r && sum>=target){
                minLength = min(minLength, r-l+1);
                sum -= nums[l];
                l++;
            }


        }
        if(minLength == INT_MAX){
            return 0;
        }
        else{
            return minLength;
        }
    }
};