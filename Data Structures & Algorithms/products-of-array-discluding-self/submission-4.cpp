#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        deque<int> suffix;
        vector<int> result;
        int products = 1;

        for(int i = 0; i<nums.size();i++){
            if(i==0){
                prefix.push_back(1);
            }
            else{
                products = nums[i-1] * products;
                prefix.push_back(products);

            }
        }
        int products1 = 1;
        for(int j = nums.size() -1; j>=0; j--){
            if(j==nums.size() -1){
                suffix.push_back(1);

            }
            else{
                products1 = products1* nums[j+1];
                suffix.push_front(products1);

            }
        }

        for(int k = 0; k<nums.size(); k++){
            result.push_back(prefix[k] * suffix[k]);
        }
        return result;


    }
};
