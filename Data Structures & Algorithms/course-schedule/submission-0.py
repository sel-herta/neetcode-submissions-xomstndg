class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            indegrees[a] += 1
        
        q = deque()

        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)
        
        taken = 0
        ans = []
        while q:
            b = q.popleft()
            taken += 1
            ans.append(b)
            for a in adjList[b]:
                indegrees[a] -= 1
                if indegrees[a] == 0:
                    # we can take
                    q.append(a)
        return taken == numCourses