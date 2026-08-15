class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<int>> anagrams;

        for(int i = 0; i<strs.size(); ++i){
            string key = strs[i];
            sort(key.begin(), key.end());

            anagrams[key].push_back(i);
        }

        vector<string> groups;
        vector<vector<string>> result;

        for(const auto& [key, value]: anagrams){
            for(int index: value){
                groups.push_back(strs[index]);
            }
            result.push_back(groups);
            groups.clear();
        }

        return result;



    }
};
