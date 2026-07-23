class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        nodes = {}
        for word in words:
            for c in word:
                nodes[c] = set()
        indegree = {}
        for c in nodes:
            indegree[c] = 0
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in nodes[w1[j]]:
                        nodes[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        q = deque()
        for c, ind in indegree.items():
            if ind == 0:
                q.append(c)

        ans = []
        while q:
            c = q.popleft()
            ans.append(c)
            for v in nodes[c]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if len(ans) != len(indegree):
            return ""
        return "".join(ans)
        