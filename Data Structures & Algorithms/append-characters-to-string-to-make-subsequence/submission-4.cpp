#include<string>
using namespace std;
class Solution {
public:
    int appendCharacters(string s, string t) {
        int index = 0;
        for(int i = 0; i<s.size(); i++){
            if(index>=t.size()){
                break;
            }
            if(s[i] == t[index]){
                index++;
            }
        }        
        int result = t.size()-index;
        return result;
        
    }
};