#include <vector>
#include <string>
using namespace std;
class Solution {
public:
    bool IsPalindrome(const string &s, int l, int r){
        while(l<r){
            if(s[l] !=s[r]){
                return false;
            }
                l++;
                r--;
        }
        return true;
            
    }
    bool validPalindrome(string s) {
        

        int l = 0;
        int r = s.size() -1;

        while(l<r){
            if(s[l] == s[r]){
                l++;
                r--;
            }
            else if(s[l] != s[r]){
                return IsPalindrome(s,l+1, r) || IsPalindrome(s,l,r-1);

            }
        }
        return true;


        
    }
};