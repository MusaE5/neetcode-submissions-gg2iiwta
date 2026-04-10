#include <unordered_map>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;

        for(int x: nums){
            freq[x]++;
        }

        priority_queue<pair<int, int>> pq;
        for(auto& p: freq){
            pq.push({p.second, p.first});
        }
        vector<int> result;
        for(int i=0; i<k; i++){
            result.push_back(pq.top().second);
            pq.pop();
        }
        return result;


        
    }
};
