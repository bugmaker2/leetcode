class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) < 3:
            return max(nums)
        amount = [0]*len(nums)
        amount[0],amount[1] = nums[0],max(nums[0],nums[1])
        for i in range(2,len(nums)):
            amount[i] = max(amount[i-1], amount[i-2] + nums[i])
        return max(amount[len(nums)-1],amount[len(nums)-2])
