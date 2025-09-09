//35. Search Insert Position
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        bool check= false;
        int n=nums.size();
        if(nums[0]>target){
            return 0;
        } 
        if(nums[n-1]<target){
            return n;
        }
        for (int i=0;i<nums.size();i++){
            if(nums[i]== target){
                check=true;
                return i;
                break;
            } else if(check==false && nums[i]>target){
                return i;
                break;
            }
        }
        return 0;
    }
};