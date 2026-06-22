class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        adjList = defaultdict(list)
        for word in wordList:
            diff = 0
            for i in range(len(word)):
                if beginWord[i] != word[i]:
                    diff += 1
            if diff == 1:
                adjList[beginWord].append(word)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                diff = 0
                for k in range(len(beginWord)):
                    if wordList[i][k] != wordList[j][k]:
                        diff += 1
                if diff == 1:
                    adjList[wordList[i]].append(wordList[j])
                    adjList[wordList[j]].append(wordList[i])
        q = deque()
        visited = set()
        q.append((beginWord, 1))
        visited.add(beginWord)
        
        while q:
            word, currTime = q.popleft()
            if word == endWord:
                return currTime
            for nextWord in adjList[word]:
                if nextWord not in visited:
                    visited.add(nextWord)
                    q.append((nextWord, currTime + 1))
        return 0