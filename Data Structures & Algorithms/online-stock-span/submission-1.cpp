class StockSpanner {
    vector<int> nums;

public:
    StockSpanner() {
    }
    
    int next(int price) {
        if(nums.empty()){
            nums.push_back(price);
            return 1;
        }
        else{
            int counter = 1;
            for(int i = nums.size() -1; i>-1; i--){
                if(nums[i] <= price){
                    counter++;
                }
                else{
                    break;
                }
            }
            nums.push_back(price);
            return counter;
        }
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */