class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> prefix;
        vector<int> suffix;
        vector<int> result;

        int product = 1;
        const int size = nums.size();

        for(int i = 0; i<size; i++){
            if(i == 0){
                prefix.push_back(1);
            }
            else{
                product *= nums[i-1];
                prefix.push_back(product);

            }
        }

        product = 1;

        for(int i =size-1;i>-1; i--){
            if(i == size-1){
                suffix.push_back(1);
            }
            else{
                product*= nums[i+1];
                suffix.push_back(product);
            }
        }
        reverse(suffix.begin(), suffix.end());

        for(int i = 0; i<size; i++){
            result.push_back(prefix[i] * suffix[i]);
        }
        return result;

        

    }
};
