class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == '+':
                if len(stack) >= 2:
                    new_num = stack[len(stack) - 1] + stack[len(stack) - 2]
                    stack.append(new_num)
            elif operation == 'D':
                if stack:
                    stack.append(stack[-1] * 2)
            elif operation == 'C':
                stack.pop()
            else:
                stack.append(int(operation))
        return sum(stack)