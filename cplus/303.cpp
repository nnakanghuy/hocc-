//303. Range Sum Query - Immutable
class NumArray {
public:
    vector<int>sums;
    NumArray(vector<int>& nums) {
        int num = 0;
        for (int i=0;i<nums.size();i++){
            num=num+nums[i];
            sums.push_back(num);
        }
    }
    
    int sumRange(int left, int right) {
        if(left ==0){
            return sums[right];
        } else{
            return sums[right] - sums[left-1];
        }
    }
};