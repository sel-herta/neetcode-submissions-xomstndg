class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # freqs of each character : anagram
        for s in strs:
            data = [0] * 26
            for l in s:
                data[ord(l) - ord("a")] += 1
            res[tuple(data)].append(s)
        return list(res.values())