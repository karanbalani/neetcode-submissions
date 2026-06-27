class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        x, y = 0, len(numbers) - 1

        while x < y:

            if numbers[x] + numbers[y] == target:
                return [x + 1, y + 1]
            
            if numbers[x] + numbers[y] > target:
                y -= 1
                continue
            
            if numbers[x] + numbers[y] < target:
                x += 1
                continue
            
        return []