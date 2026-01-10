#84. Largest Rectangle in Histogram
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        rec = 0
        stack = []
        for i, v in enumerate(heights):
            while stack and heights[stack[-1]] > v:
                height = heights[stack[-1]]
                stack.pop()
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                rec = max(rec, height*width)
            stack.append(i)
        return rec