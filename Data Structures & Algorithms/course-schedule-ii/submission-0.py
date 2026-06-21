class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        adjList = defaultdict(list)
        indegrees = [0] * numCourses

        for a, b in prerequisites:
            adjList[b].append(a)
            indegrees[a] += 1
        
        q = deque()
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                q.append(i)
        
        while q:
            b = q.popleft()
            ans.append(b)
            for a in adjList[b]:
                indegrees[a] -= 1
                if indegrees[a] == 0:
                    q.append(a)
        if len(ans) == numCourses:
            return ans
        else:
            return []