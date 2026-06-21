class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        add = lambda a,b: a + b
        sub = lambda a,b: a - b
        mult = lambda a,b: a * b
        div = lambda a,b: int(a/b)
        ops = {'+': add, '-': sub, '*': mult, '/': div}

        stack = []
        ans = 0
        for i in tokens:
            if not i in ops:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(ops[i](a,b))

        return stack[-1]