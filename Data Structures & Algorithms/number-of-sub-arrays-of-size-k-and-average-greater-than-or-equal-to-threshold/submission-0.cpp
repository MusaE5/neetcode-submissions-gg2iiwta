class Solution {
public:
    int numOfSubarrays(vector<int>& arr, int k, int threshold) {
        int l = 0;
        double sum = 0;
        int counter = 0;
        
        for(int r=0; r<arr.size(); r++){
            while(r-l >= k){
                sum-= arr[l];
                l++;
            }
            sum+= arr[r];
            if(r-l == k-1){
                if(sum / k >= threshold){
                    counter++;
                }
            }

            
        }
        return counter;
    }
};