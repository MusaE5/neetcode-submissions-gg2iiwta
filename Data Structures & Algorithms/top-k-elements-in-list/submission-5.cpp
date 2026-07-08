class Solution {
public:

    static bool compareByValue(const pair<int,int>& a, const pair<int,int>& b){
            return a.second > b.second;
        }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> result;
        unordered_map<int,int> freq;

        for(int num: nums){
            freq[num] ++;
        }
        // Copy items into vector
        vector<pair<int, int>> vec(freq.begin(), freq.end());

        // Third argument must match 
        // bool functionName(const Type& a, const Type& b)
        // return true if the first argument should apear before the second
        // return false if the first argument should appear after the second
        sort(vec.begin(), vec.end(), compareByValue);
        
        int counter = 0;
        for(auto& topK: vec){
            if(counter>= k){
                return result;
            }
            result.push_back(topK.first);
            counter++;
        }

    
    }

};
