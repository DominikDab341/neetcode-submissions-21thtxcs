class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            left = i-1
            right = i+1
            result = 1
            while left >= 0:
                result *= nums[left]
                left -= 1
            while right < len(nums):
                result*=nums[right]
                right += 1 
            output.append(result)
        return output
