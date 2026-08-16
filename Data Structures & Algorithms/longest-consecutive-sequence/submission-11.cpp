class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if(nums.size() == 0){
            return 0;
        }

        unordered_set<int> s;
        for(int i: nums){
            s.insert(i);
        }

        int result = 1;
        int counter = 1;
        for(int i: nums){
            if(!s.contains(i-1)){
                while(s.contains(i+1)){
                    counter++;
                    i++;
                }
                result = max(result, counter);
                counter = 1;
            }
        }

        return result;
    }
};
