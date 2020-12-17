class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = ''
        for i in S:
            if i == '(':
                stack.append('(')
                if len(stack) > 1:
                    result += '('
            if i == ')':
                stack.pop()
                if len(stack) != 0:
                    result += ')'
        return result
