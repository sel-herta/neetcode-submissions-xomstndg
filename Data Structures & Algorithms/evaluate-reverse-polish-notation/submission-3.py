class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opperands = ["+", "-", "*", "/"]
        for c in tokens:
            if c not in opperands:
                stack.append(int(c))
            else:
                n_2, n_1 = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(n_1 + n_2)
                elif c == '-':
                    stack.append(n_1 - n_2)
                elif c == '*':
                    stack.append(n_1 * n_2)
                elif c == '/':
                    stack.append(int(n_1 / n_2))

        return stack[-1]