class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums.sort()

        for idx in range (len(nums)) :
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            # now this becomes a two sum problem
            x, y = idx + 1, len(nums) - 1

            while x < y:

                # best case
                if nums[idx] + nums[x] + nums[y] == 0:
                    result.append([nums[idx], nums[x], nums[y]])
                    
                    x += 1
                    while nums[x] == nums[x-1] and x < y:
                        x += 1

                    continue
                
                if nums[idx] + nums[x] + nums[y] > 0:
                    y -= 1
                    continue
                
                if nums[idx] + nums[x] + nums[y] < 0:
                    x += 1
                    continue
                
        return result
