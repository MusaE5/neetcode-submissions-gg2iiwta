class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";

        for(int i = 0; i<strs[0].size(); i++){
            char c = strs[0][i];

            for(int s = 0; s<strs.size(); s++){
                if(i >= strs[s].size() || strs[s][i] != c){
                    return prefix;
                }
            }
            prefix += c;

        }
        return prefix;
    }
};