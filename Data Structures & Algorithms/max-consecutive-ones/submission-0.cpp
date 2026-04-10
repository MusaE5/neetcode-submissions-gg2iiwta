
class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int result = 0;
        int counter = 0;

        for(int i = 0; i <nums.size(); i++){
            if(nums[i] != 1){
                counter = 0;
            }
            else{
                counter ++;
                result = max(result, counter);
            }

        }
        return result;
        
    }
};