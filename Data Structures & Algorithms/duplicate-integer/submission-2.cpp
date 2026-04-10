#include <vector>
#include <unordered_set>
using namespace std;
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> dupes;

        for(int x : nums){
            if(dupes.count(x)){
                return true;

            }
            dupes.insert(x);  
            }
            
        return false;
        }  
    };
