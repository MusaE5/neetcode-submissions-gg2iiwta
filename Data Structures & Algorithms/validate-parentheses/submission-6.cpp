class Solution {
public:
    bool isValid(string s) {

        unordered_map<char, char> symbols{{'(',')'}, {'[',']'}, {'{','}'}}; 
        stack<char> st;

        for(char c: s){
            if(symbols.contains(c)){
                st.push(c);
            }
            else{
                if(st.empty() || symbols[st.top()] != c){
                    return false;
                }
                st.pop();
            }
        }

        return st.empty();


    }
};
