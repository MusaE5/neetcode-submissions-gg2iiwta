#include <vector>
#include <unordered_map>
#include <string>
using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> freq;

        for(char c:s){
            if(freq.count(c) == 0){
                freq[c] = 1;

            }
            else{
                freq[c]++;
            }
        }

        for(char a:t){
            if(freq.count(a) == 0){
                return false;
            }
            else{
                freq[a]--;
            }

        }

        for(auto& p: freq){
            if(p.second !=0){
                return false;
            }
        }
        return true;


        
    }
};
