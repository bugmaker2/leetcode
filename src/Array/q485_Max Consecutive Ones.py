class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = -1
        max1 = 0
        if len(nums) == 0:
            return 0

        i, j = 0, 0
        while i < len(nums):
            if nums[i] != 1:
                i += 1
            else:
                j = i
                count = 0
                while j < len(nums) and nums[j] == 1:
                    count += 1
                    j += 1
                max1 = max(max1, count)
                i = j

                
        return max1
