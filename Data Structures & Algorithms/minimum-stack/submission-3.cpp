#include<cstdint>
class MinStack {
    stack<int> myStack;
    stack<int> minStack;

    public:   
    
    void push(int val) {
        myStack.push(val);

        if(!minStack.empty()){
            if(val<= minStack.top()){
                minStack.push(val);
            }
        }

        else{
            minStack.push(val);
        }
    }
    
    void pop() {
        int32_t temp = myStack.top();
        myStack.pop();
        if(temp == minStack.top()){
            minStack.pop();
        }
    }
    
    int top() {
        return myStack.top();
    }
    
    int getMin() {
        return minStack.top();
    }
};
