//27. Remove Element
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int n=nums.size();
        if(n==0){
            return 0;
        }
        int kq=0;
        int l=0;
        int r=n-1;
        while(l<r){
            if(nums[l]==val && nums[r]!= val){
                swap(nums[l],nums[r]);
                l++;
            } else if(nums[l]==val && nums[r]==val){
                r--;
            } else if(nums[l]!= val && nums[r]!=val){
                l++;
            } else{
                r--;
            }
        }
        for(int i=0;i<n;i++){
            if(nums[i]!=val){
                kq++;
            }
        }
        return kq;
    }
};