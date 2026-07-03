class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> anagrams;

        vector<vector<string>> result;

        for(string x: strs){
            string key = x;
            sort(key.begin(), key.end());
            anagrams[key].push_back(x);
        }

        for(pair<const string, vector<string>>& element: anagrams){
            result.push_back(element.second);
        }

        return result;
        
    }
};
