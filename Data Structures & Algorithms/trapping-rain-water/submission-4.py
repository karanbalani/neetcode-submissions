class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []

        temp_max = height[0]
        max_left.append(temp_max)
        for i in range (1, len(height)):
            temp_max = max(temp_max, height[i])
            max_left.append(temp_max)
        
        temp_max = height[-1]
        max_right.append(temp_max)
        for i in range (len(height) - 2, -1, -1):
            temp_max = max(temp_max, height[i])
            max_right.insert(0, temp_max)

        res = 0

        for idx, num in enumerate(height):

            # how much water can be trapped at position i?
            water = min(max_left[idx], max_right[idx]) - num

            res += water
        
        return res
