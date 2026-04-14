class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i, c in enumerate(word):
            if not curr.nxt[ord(c)%32 - 1]: 
                curr.nxt[ord(c)%32 - 1] = TrieNode(c)
            if i == len(word)-1: 
                curr.nxt[ord(c)%32 - 1].makeEnd()
            curr = curr.nxt[ord(c)%32 - 1]

    def search(self, word: str) -> bool:
        curr = self.root
        for i, c in enumerate(word):
            curr = curr.nxt[ord(c)%32 - 1]
            if not curr: 
                return False
            elif i == len(word)-1 and curr.isEnd:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix: 
            curr = curr.nxt[ord(c)%32 - 1]
            if not curr: 
                return False
        return True

class TrieNode:
    def __init__(self, letter="", isEnd=False):
        self.letter = letter
        self.nxt = [None] * 26
        self.isEnd = isEnd
    
    def setNext(self, nxt):
        self.nxt[ord(nxt.letter)%32 - 1] = nxt
    def makeEnd(self):
        self.isEnd = True
