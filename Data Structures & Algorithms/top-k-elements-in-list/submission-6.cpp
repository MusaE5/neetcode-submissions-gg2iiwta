class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> freq;
        for(int i: nums){
            freq[i]++;
        }
        // copy elements into vector to be sorted. 
        vector<pair<int,int>> vec(freq.begin(), freq.end());

        // sort in descending order (return true for what you want to be first)
        sort(vec.begin(), vec.end(), [](const auto& a, const auto& b){
            return a.second > b.second;
        } );

        vector<int> result;
        for(int i = 0; i<k; ++i){
            result.push_back(vec[i].first);
        }

        return result;






    }
};
