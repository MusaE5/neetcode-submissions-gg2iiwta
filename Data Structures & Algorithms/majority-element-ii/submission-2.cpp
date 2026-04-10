#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        vector<int> result;
        unordered_map<int,int> freq;
        const int size = nums.size();
        const int amount = size/3;

        for(int i: nums){
            freq[i] ++;
        }

        for(auto &[key, value]: freq){
            if(value>amount){
                result.push_back(key);
            }

        }
        return result;
    }
};