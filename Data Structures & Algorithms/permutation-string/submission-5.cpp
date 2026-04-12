#include<unordered_map>
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char,int> freq;

        for(char i: s1){
            freq[i] ++;
        }

        int l = 0;

        for(int r = 0; r<s2.size(); r++){
            if(freq.count(s2[r])){
                freq[s2[r]] --;
            }
            if(r-l+1> s1.size()){
                
                if(freq.count(s2[l])){
                    freq[s2[l]]++;
                }
                l++;
            }
            bool alert = true;
            for(auto &[key,value]: freq){
                if(value!=0){
                    alert = false;
                }
            }
            if(alert){
                return true;
            }


        }
        return false;
    }
};
