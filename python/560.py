#560. Subarray Sum Equals K
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        current_sum = 0
        prefix_count = {0:1}
        for num in nums:
            current_sum +=num
            if current_sum - k in prefix_count:
                count +=prefix_count[current_sum - k]
            prefix_count[current_sum] = prefix_count.get(current_sum,0) +1
        return count