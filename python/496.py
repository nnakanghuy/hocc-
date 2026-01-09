#496. Next Greater Element I
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        st = []
        ans = []
        for v in nums1:
            st.append(v)
            for i in range(len(nums2)):
                if nums2[i] == v:
                    if i == len(nums2)-1:
                        ans.append(-1)
                        st.pop()
                        break
                    else:
                        tmp = i+1
                        break
            while st:
                if nums2[tmp] > v:
                    ans.append(nums2[tmp])
                    st.pop()
                else:
                    tmp = tmp+1
                if tmp >= len(nums2):
                    ans.append(-1)
                    st.pop()
        return ans
            