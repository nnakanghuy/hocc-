//34. Find First and Last Position of Element in Sorted Array
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>kq={-1,-1};
        int l=0;
        int r=nums.size()-1;
        bool check1=false;
        bool check2=false;
        if (nums.empty()) return kq;
        if((l==0 && nums[l]>target) || (r==nums.size()-1 && nums[r]<target)){
            return kq;
        }
        while(l<=r){
            if(nums[l]<target){
                l++;
            } else if(nums[l]==target){
                kq[0]=l;
                check1=true;
            }
            if(nums[r]>target){
                r--;
            } else if(nums[r]==target){
                kq[1]=r;
                check2=true;
            }
            if(check1==true && check2==true){
                break;
            }
        }
        return kq;
    }
};