class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if(nums.size() == 0){
            return 0;
        }

        if(nums.size() == 1){
            return (nums[0] == k);
        }

        int result = 0;
        int r = 0;
        int current_sum = 0;

        for(int i = 0; i<nums.size(); ++i){

            if(i == nums.size() -1){
                if(nums[i] == k){
                    result++;
                }
                break;
            }

            if(nums[i] == k){
                result++;
            }

            current_sum = nums[i];
            r = i+1;

            while(r<nums.size()){
                current_sum += nums[r];
                if(current_sum == k){
                    result++;
                }
                r++;
            }

        }

        return result;
    }
};