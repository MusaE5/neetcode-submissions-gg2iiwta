class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_set<char> check;

        // rows
        for(const auto& row: board){
            for(const auto& c: row){
                if(!isdigit(c)){
                    continue;
                }

                if(check.contains(c)){
                    return false;
                }
                check.insert(c);
            }
            check.clear();
        }

        // columns
        for(int i = 0; i<board.size(); ++i){
            for(const auto& row: board){

                if(!isdigit(row[i])){
                    continue;
                }

                if(check.contains(row[i])){
                    return false;
                }
                check.insert(row[i]);

            }
            check.clear();
        }

        // 3x3 boxes
        int counter = 1;
        vector<int> rows{0,1,2};

        while(counter <=3){
            for(int i = 0; i<board.size(); ++i){
                if(i== 0 ||i == 3 || i == 6){
                    check.clear();
                }
                for(int r: rows){
                    if(!isdigit(board[r][i])){
                        continue;
                    }

                    if(check.contains(board[r][i])){
                        return false;
                    }

                    check.insert(board[r][i]);
                }

            }

            counter ++;
            for(auto& row: rows){
                row+=3;
            }

        }    

        return true;

    }
};
