class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            row = matrix[i]
            # binary search
            l, r = 0, len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] > target:
                    r = m - 1
                elif row[m] < target:
                    l = m + 1
                else:
                    return True
        return False