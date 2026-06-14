class Node:
    def __init__(self):
        self.isWord = False
        self.wordIndex = -1
        self.children = defaultdict(Node)

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insertWord(self, word, wordIndex):
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True
        curr.wordIndex = wordIndex

    def search(self, word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return -2
        return curr.wordIndex

    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return False
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for i, word in enumerate(words):
            trie.insertWord(word, i)
        rows, cols = len(board), len(board[0])
        ans = []
        currPath = set()
        addedWords = set() # avoid dupes
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(i, j, currNode):
            if currNode.isWord and currNode.wordIndex not in addedWords:
                addedWords.add(currNode.wordIndex)
                ans.append(words[currNode.wordIndex])
            for ci, cj in dirs:
                ni, nj = i + ci, j + cj
                if 0 <= ni < rows and 0 <= nj < cols:
                    if (ni, nj) not in currPath:
                        if board[ni][nj] in currNode.children:
                            currPath.add((ni, nj))
                            dfs(ni, nj, currNode.children[board[ni][nj]])
                            currPath.remove((ni, nj))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in trie.root.children:
                    currPath.add((i, j))
                    dfs(i, j, trie.root.children[board[i][j]])
                    currPath.remove((i, j))
        return ans
