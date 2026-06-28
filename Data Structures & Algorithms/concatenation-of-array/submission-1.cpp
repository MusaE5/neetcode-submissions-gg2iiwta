class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans;
        int counter = 0;

        while(counter<=1){
            for(int num:nums){
                ans.push_back(num);
            }
            counter ++;
        }

        return ans;
        
    }
};