#643. Maximum Average Subarray I
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        win_first = sum(nums[:k])
        maxi = win_first
        for i in range(k,len(nums)):
            win_first += nums[i] - nums[i-k]
            if win_first > maxi:
                maxi = win_first
        return maxi/float(k)