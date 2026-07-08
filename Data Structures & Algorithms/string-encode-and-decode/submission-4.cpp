class Solution {
public:

    string encode(vector<string>& strs) {
        string result = "";
        for(string& s: strs){
            string len = to_string(s.size());
            result += len + '#' + s;
        }

        return result;
    }

    vector<string> decode(string s) {
        vector<string> result;
        int i = 0;
        while(i<s.size()){

            int slash = s.find('#', i);

            int len = stoi(s.substr(i, slash-i));

            result.push_back(s.substr(slash+1, len));

            i = slash + len+1; // go to slash, skip the length +1
        }
        return result;    

        
    }
};
