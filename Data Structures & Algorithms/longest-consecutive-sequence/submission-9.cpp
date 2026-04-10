#include<unordered_set>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int max_len = 0;
        int len = 0;
        unordered_set<int> unique;

        for(int i:nums){
            unique.insert(i);
        }

        for(int j:nums){
            if(unique.count(j-1) == 0){
                len = 1;
                int cur_num = j;
                while(unique.count(cur_num+1)){
                    len++;
                    cur_num++;
                }
            }
            max_len = max(max_len, len);

        }
        return max_len;


        
    }
};
