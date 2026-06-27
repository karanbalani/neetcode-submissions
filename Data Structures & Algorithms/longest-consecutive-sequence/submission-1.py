class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        count = 0

        for num in nums:
            # check if this number is a start of the possible sequence
            # means num - 1 (the left neighbour) would not be present in the set
            if num - 1 in nums_set:
                continue # this is not the start of a possible sequence
            
            # sequence has started
            new_seq_count = 1
            
            next_num = num + 1
            while next_num in nums_set:
                new_seq_count += 1
                next_num += 1
            
            if new_seq_count > count:
                count = new_seq_count
        
        return count