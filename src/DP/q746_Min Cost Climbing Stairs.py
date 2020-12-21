class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        price = [None]*len(cost)
        if len(cost) <=1:
            return 0
        price[0] = cost[0]
        price[1] = cost[1]
        for i in range(2,len(cost)):
            price[i] = cost[i] + min(price[i-1],price[i-2])
        return min(price[len(cost)-1],price[len(cost)-2])
