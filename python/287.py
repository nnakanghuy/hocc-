#287. Find the Duplicate Number
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        store = set()
        for x in nums:
            if x in store:
                return x
            store.add(x)