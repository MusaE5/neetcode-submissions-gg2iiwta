class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int counter = 0;

        for(int i = 0; i<nums.size(); i++){
            if(nums[i] == k){
                counter++;
            }
            
                int target = k - nums[i];
                int win_sum = 0;
                for(int r = i+1; r<nums.size(); r++){
                    win_sum += nums[r];
                    if(win_sum == target){
                        counter++;
                    }
                }
            
        }
        return counter;
        
    }
};