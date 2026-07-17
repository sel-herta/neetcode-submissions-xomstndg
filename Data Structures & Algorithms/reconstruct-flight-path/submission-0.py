class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        tickets.sort()
        for u, v in tickets:
            adj_list[u].append(v)
        
        res = ["JFK"]
        def dfs(u):
            if len(res) == len(tickets) + 1:
                return True
            if u not in adj_list:
                return False
            tmp = list(adj_list[u])
            for i, v in enumerate(tmp):
                adj_list[u].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj_list[u].insert(i, v)
                res.pop()
        dfs("JFK")
        return res

