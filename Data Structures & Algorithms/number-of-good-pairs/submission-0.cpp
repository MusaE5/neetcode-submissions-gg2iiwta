class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {

        unordered_map<int,int> seen;

        for(int i: nums){
            seen[i] ++;
        }

        int result = 0;

        // 1 occurance = 0;
        // 2 occurances = 1;
        // 3 occurances = 3
        // 4 occurances = 6

        for(const auto& [key,value]: seen){
            if(value == 1){
                continue;
            }
            result += (value * (value-1) /2); // something
        }

        return result;
    }
};