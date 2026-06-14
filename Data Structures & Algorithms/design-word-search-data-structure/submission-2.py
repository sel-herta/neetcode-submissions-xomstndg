class Node:
    def __init__(self):
        self.isWord = False
        self.children = defaultdict(Node)
    
# . counts for any word

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children[char]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        res = self.searchFrom(word, curr)
        if res and res.isWord == True:
            return True
        else:
            return False
    
    def searchFrom(self, word, currNode):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        if not word:
            return currNode
        if word[0] == ".":
            for char in alphabet:
                if char in currNode.children:
                    res = self.searchFrom(word[1:len(word)], currNode.children[char])
                    if res:
                        return res
        if word[0] in currNode.children:
            res = self.searchFrom(word[1:len(word)], currNode.children[word[0]])
            return res
        else:
            return None
