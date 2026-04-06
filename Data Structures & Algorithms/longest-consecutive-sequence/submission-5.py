class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        potential_max_sequence = 1
        max_sequence = 0 
        if len(nums)==1: 
            return 1

        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                potential_max_sequence += 1
            else:
                potential_max_sequence = 1 
            if potential_max_sequence > max_sequence:
                max_sequence = potential_max_sequence
        return max_sequence