class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        prefix = []
        
        pref_temp = 1
        for n in nums:
            pref_temp *= n
            prefix.append(pref_temp)
        
        postfix = []
        
        post_temp = 1
        for i in range (len(nums)-1, -1, -1):
            post_temp *= nums[i]
            postfix.insert(0, post_temp)
        
        print(prefix)
        print(postfix)

        result = []

        for i in range (0, len(nums)):
            if i == 0:
                result.append(postfix[i+1])
                continue
            
            if i == len(nums) - 1:
                result.append(prefix[i-1])
                continue
            
            result.append(prefix[i-1] * postfix[i+1])

        return result