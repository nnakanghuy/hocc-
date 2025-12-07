#202. Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        store = set()
        x = n
        total = 0
        while True:
            total = sum(int(ch)**2 for ch in str(x))
            if total == 1:
                return True
            if total in store:
                return False

            store.add(total)
            x = total