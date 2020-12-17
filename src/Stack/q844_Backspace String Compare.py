class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack1 = []
        stack2 = []
        for i in range(len(S)):
            if S[i] == '#' and stack1!=[]:
                stack1.pop()
            elif S[i] != '#':
                stack1.append(S[i])
        for i in range(len(T)):
            if T[i] == '#' and stack2!=[]:
                stack2.pop()
            elif T[i] != '#':
                stack2.append(T[i])
        return stack1 == stack2
