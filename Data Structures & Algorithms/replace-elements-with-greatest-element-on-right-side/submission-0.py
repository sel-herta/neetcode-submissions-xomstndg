class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        suffixMax = [0] * (len(arr) + 1)
        for i in range(len(arr) - 1, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], arr[i])
        ans = []
        for i in range(1, len(arr)):
            ans.append(suffixMax[i])
        ans.append(-1)
        return ans