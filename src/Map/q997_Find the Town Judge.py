class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        cir = [0,0]*N
        for i in range(len(trust)):
            cir[(trust[i][0]-1)*2] += 1
            cir[(trust[i][1]-1)*2+1] += 1
        for i in range(N):
            if cir[i*2] == 0 and cir[i*2+1] == N-1:
                return i+1
        return -1
