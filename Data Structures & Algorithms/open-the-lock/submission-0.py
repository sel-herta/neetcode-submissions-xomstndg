class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        target = list(target)
        adj = defaultdict(list)
        deadend = set()

        for comb in deadends:
            l = list(comb)
            deadend.add(tuple(l))

        if ('0', '0', '0', '0') in deadend:
            return -1

        for num in range(10):
            a1 = (num-1) % 10
            a2 = (num+1) % 10
            adj[str(num)].append(str(a1))
            adj[str(num)].append(str(a2))
        
        q = deque()
        q.append((['0', '0', '0', '0'], 0))
        visited = set()
        visited.add(('0', '0', '0', '0'))

        while q:
            u, moves = q.popleft()
            if u == target:
                return moves
            for i, digit in enumerate(u):
                for v in adj[digit]:
                    new_u = u[:i] + [v] + u[i+1:]
                    tup = tuple(new_u)
                    if tup in deadend:
                        continue
                    if tup not in visited:
                        visited.add(tup)
                        q.append((new_u, moves + 1))
        return -1