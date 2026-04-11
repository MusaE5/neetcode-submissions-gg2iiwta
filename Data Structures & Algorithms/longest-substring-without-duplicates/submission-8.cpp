#include<unordered_set>
#include<string>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_set<char> window;
      
        int l = 0;
        int length = 0;

        for(int r = 0; r<s.size(); r++){
            while(window.count(s[r])){
                window.erase(s[l]);
                l++;
            }
            window.insert(s[r]);
            length = max(length, (int)window.size());

        }
        return length;
    }
};
