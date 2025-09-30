#two sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i in range(len(nums)):
            temp=target - nums[i]
            if nums[i] in result:
                return (result[nums[i]],i)
            result[temp]=i
        return [-1,-1]