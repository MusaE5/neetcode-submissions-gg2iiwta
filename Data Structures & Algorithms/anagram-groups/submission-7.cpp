#include<unordered_map>
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> hashmap;
        vector<vector<string>> result;

        for(int i = 0; i <strs.size(); i++){
            string key = strs[i];
            sort(key.begin(), key.end());
            hashmap[key].push_back(strs[i]);
        }
        for(auto& [k,v] : hashmap){
            result.push_back(v);
        }
        return result;
    }
};
