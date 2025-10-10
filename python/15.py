#15. 3Sum
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        kq = []
        numss = sorted(nums)
        n = len(numss)
        for i in range(n-2):
            if i > 0 and numss[i] == numss[i-1]:
                continue
            lp = i + 1
            rp = n - 1
            while lp < rp:
                total =numss[i] + numss[lp] + numss[rp]
                if total <0:
                    lp+=1
                elif total > 0:
                    rp-=1
                else:
                    kq.append((numss[i],numss[lp],numss[rp]))
                    while (lp < rp and numss[lp] == numss[lp+1]):
                        lp +=1
                    while (lp < rp and numss[rp] == numss[rp-1]):
                        rp -=1
                    lp+=1
                    rp-=1
        return kq