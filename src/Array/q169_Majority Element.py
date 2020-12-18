class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == major:
                count += 1
            else:
                count -= 1
            if count == 0:
                major = nums[i]
                count = 1
        return major
