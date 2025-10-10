#167. Two Sum II - Input Array Is Sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        lp = 0
        rp = len(numbers) - 1
        kq = []
        while(lp < rp):
            if numbers[lp] + numbers[rp] == target:
                lp+=1
                rp+=1
                kq.append(lp)
                kq.append(rp)
                break
            elif numbers[lp] + numbers[rp] < target:
                lp +=1
            else:
                rp -=1
        return kq