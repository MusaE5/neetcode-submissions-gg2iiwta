class MinStack{
    stack<int> mins;
    stack<int> myStack;
    public:

    void push(int val) {
        myStack.push(val);
        if(!mins.empty()){
            if(mins.top() >= val){
                mins.push(val);
            }
        }
        else{
            mins.push(val);
        }
    }
    
    void pop() {
        int temp = myStack.top();
        myStack.pop();
        if(!mins.empty() && temp == mins.top()){
            mins.pop();
        }
        
    }
    
    int top() {
        return myStack.top();
    }
    
    int getMin() {
        return mins.top();
    }

};
