#303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums =nums

    def sumRange(self, left: int, right: int) -> int:
        self.left=left
        self.right=right
        tong=0
        sum_nums=[]
        for i in range(len(self.nums)):
            tong+=self.nums[i]
            sum_nums.append(tong)
        if (left >0):
            kq=sum_nums[right]-sum_nums[left-1]
        else:
            kq=sum_nums[right]
        return kq

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)