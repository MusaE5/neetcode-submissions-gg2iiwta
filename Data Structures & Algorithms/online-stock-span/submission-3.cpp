class StockSpanner {
    stack<pair<int,int>> s;

public:
    StockSpanner() {
        
    }
    
    int next(int price) {
        if(s.empty()){
            s.push({price, 1});
            return s.top().second;
        }
        else{
            int spanner = 1;
            while(!s.empty() && price>= s.top().first){
                spanner += s.top().second;
                s.pop();
            }
            s.push({price, spanner});
            return spanner;
        }
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */