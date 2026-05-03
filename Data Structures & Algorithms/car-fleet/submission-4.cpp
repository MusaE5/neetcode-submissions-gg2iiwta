class Solution {
public:
    int carFleet(int& target, vector<int>& position, vector<int>& speed) {
        stack<pair<int,int>> st;
        unordered_map<int, int> car;

        for(int i = 0; i<position.size(); i++){
            car[position[i]] = speed[i];
        }

        sort(position.rbegin(), position.rend());

        // hours to reach end : (double(target) - position )/speed

        for(int num: position){
            if(st.empty()){
                st.push({num, car[num]});
            }

            else{
                double hours = (double(target) - num)/ car[num];
                if(!st.empty() && ((double(target) - st.top().first) / st.top().second) < hours){
                    st.push({num, car[num]});
                }
            }
        }
        return st.size();
    }
};
