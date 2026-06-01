class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tk in tokens:
            if tk not in '+-*/': stack.append(int(tk))
            else:
                b = stack.pop()
                a = stack.pop()
                if tk == '+': stack.append(a + b)
                if tk == '-': stack.append(a - b)
                if tk == '*': stack.append(a * b)
                if tk == '/': stack.append(int(a / b))

        return stack[0]