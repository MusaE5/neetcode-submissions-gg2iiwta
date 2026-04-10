#include<map>
#include<string>
#include<algorithm>
using namespace std;
class Solution {
public:
    int maxDifference(string s) {
        map<char,int> freq;
        for(char c: s){
            freq[c]++;
        }
        int maxOdd = 0;
        int minEven = 101;

        for(const auto& pair : freq){
            if(pair.second %2 == 0){
                minEven = min(minEven,pair.second);
            }
            else{
                maxOdd = max(maxOdd, pair.second);
            }
        }
        return maxOdd-minEven;
    }
};