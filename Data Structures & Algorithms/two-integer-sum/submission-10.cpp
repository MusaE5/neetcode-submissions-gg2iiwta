class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> m;
        vector<int> result;


        for(int i = 0; i <nums.size(); i++){
            int complement = target - nums[i];
            if(m.contains(complement)){
                result.push_back(m[complement]);
                result.push_back(i);
                return result;
            }
            else{
                m[nums[i]] = i;
            }
        }


    }
};
