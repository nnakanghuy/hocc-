#11. Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lp = 0
        rp = len(height) - 1
        maxi = 0
        while lp < rp:
            w = rp - lp
            h = min(height[lp],height[rp])
            area = w*h
            maxi = max(maxi, area)
            if (height[lp] <height[rp]):
                lp +=1
            else:
                rp-=1
        return maxi