#include <vector>
#include <unordered_map>
#include <string>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<int>> mp;
        vector<vector<string>> result;


        for(int i =0; i<strs.size(); i++){
            string s =strs[i];
            sort(s.begin(), s.end());
            mp[s].push_back(i);  
        }
        for(auto& p: mp){
            vector<string> sub_arr;
            for(int x: p.second){
                sub_arr.push_back(strs[x]);

            }
            result.push_back(sub_arr);
        }

        return result;

    
        
    }
};
