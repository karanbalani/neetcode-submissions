class Solution:
    def maxArea(self, heights: List[int]) -> int:
        x, y = 0, len(heights) - 1

        res = 0

        while x < y:

            # max water between two bars is basically the area
            length = y - x
            height = min(heights[x], heights[y])

            area = length * height

            if area > res:
                res = area
            
            if heights[x] > heights[y]:
                y -= 1
            else:
                x += 1
            
        return res