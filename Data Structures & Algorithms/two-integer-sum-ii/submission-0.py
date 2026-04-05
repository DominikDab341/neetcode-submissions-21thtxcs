class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l<r:
            potential_target = numbers[l]+numbers[r]
            if potential_target==target:
                return [l+1,r+1] 
            if potential_target<target:
                l+=1
            if potential_target>target:
                r-=1
