class Solution:
    def calPoints(self, ops: List[str]) -> int:
        record = []
        for s in ops:
            if s == 'C':
                record.pop()
            elif s == 'D':
                record.append(record[-1]*2)
            elif s == '+':
                record.append(record[-1]+record[-2])
            else:
                record.append(int(s))
        sum = 0
        for s in record:
            sum = sum + s
        return sum
