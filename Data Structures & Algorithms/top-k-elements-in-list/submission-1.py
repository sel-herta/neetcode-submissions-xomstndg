class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {} # num : freq
        freq_map = {} # freq : list of nums
        for i in range(len(nums) + 1):
            freq_map[i] = []
        for num in nums:
            num_map[num] = 1 + num_map.get(num, 0)
        for num, c in num_map.items():
            freq_map[c].append(num)
        
        printing = []
        for j in range(len(freq_map) - 1, 0, -1):
            for num in freq_map[j]:
                printing.append(num)
                if len(printing) == k:
                    return printing

        