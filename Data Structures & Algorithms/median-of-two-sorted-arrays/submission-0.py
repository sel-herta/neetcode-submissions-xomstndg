class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            mA = (l + r) // 2 # Mid point index of A partition
            mB = half - mA - 2 # Mid point index of B partition

            AVal = A[mA] if mA >= 0 else float('-inf')
            BVal = B[mB] if mB >= 0 else float('-inf')
            ARight = A[mA + 1] if mA + 1 < len(A) else float('inf')
            BRight = B[mB + 1] if mB + 1 < len(B) else float('inf')

            if AVal <= BRight and BVal <= ARight:
                if total % 2 == 1:
                    # odd
                    return min(ARight, BRight)
                return (max(AVal, BVal) + min(ARight, BRight)) / 2
            elif AVal > BRight:
                r = mA - 1
            else:
                l = mA + 1
                
