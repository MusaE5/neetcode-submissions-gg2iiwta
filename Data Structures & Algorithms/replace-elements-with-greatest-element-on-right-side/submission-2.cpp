#include<vector>
#include<array>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
        int currentMax = arr[arr.size()-1];
        for(int i = arr.size()-2; i>=0; i--){
            int currentNum = arr[i];
            arr[i] = currentMax;
            currentMax = max(currentMax, currentNum);

        }
        arr[arr.size()-1] = -1;
        return arr;

        
    }
};