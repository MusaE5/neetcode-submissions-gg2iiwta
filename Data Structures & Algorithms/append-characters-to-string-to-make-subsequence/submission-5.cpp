#include <string>
using namespace std;
class Solution {
public:
    int appendCharacters(string s, string t) {


int l = 0;
int r = 0;

while(r<t.size() && l<s.size()){
    if(l>s.size()){
        break;
    }

    if(s[l] == t[r]){
        r++;
    }
    l++;
}
int result = t.size() -r;
return result;
}
};