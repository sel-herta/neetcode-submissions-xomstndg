class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        # cant sort (o nlogn)
        # cant double iterate (o n^2)
        # goal o(n)
        stack = []
        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                while stack and temp > stack[-1][1]:
                    s = stack.pop()
                    ans[s[0]] = i - s[0]
                stack.append((i, temp))
        return ans


            
            