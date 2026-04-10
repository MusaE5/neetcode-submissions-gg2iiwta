#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> st;
        int max_counter = 0;

        for(int x: nums){
            st.insert(x);
        }

        for(int i: nums){
            int counter = 0;
            if(st.count(i-1) == 0){
                counter++;
                int num = i+1;
                while(st.count(num)){
                    counter++;
                    num++;
                }


            }
            max_counter = max(max_counter, counter);
        }
        return max_counter;
        
    }
};
