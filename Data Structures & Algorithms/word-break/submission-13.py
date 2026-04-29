class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.addWord(word)
        
        dp = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            
            node = trie.root
            
            for j in range(i, len(s)):
                if s[j] not in node.node:
                    break
                node = node.node[s[j]]
                
                if node.is_end and dfs(j + 1):
                    dp[i] = True
                    return True
            
            dp[i] = False
            return False
        
        return dfs(0)


class Trie: 
    def __init__(self):
        self.root = TrieNode()
        self.dp = {}
    
    def addWord(self, word):
        curr = self.root
        for c in word: 
            if c not in curr.node: 
                curr.node[c] = TrieNode()
            curr = curr.node[c]
        curr.is_end = True
        return
    
    def search(self, word, it, curr_trie):
        if it in self.dp: return self.dp[it]
        if it >= len(word): return False
        c = word[it]
        self.dp[it] = False
        
        if c in curr_trie.node:
            if it == len(word)-1 and curr_trie.node[c].is_end: 
                self.dp[it] = True
            elif curr_trie.node[c].is_end and it+1 <= len(word) and word[it+1] in curr_trie.node[c].node:
                self.dp[it] = self.dp[it] or self.search(word, it+1, curr_trie.node[c]) or self.search(word, it+1, self.root)
            elif curr_trie.node[c].is_end:
                self.dp[it] = self.dp[it] or self.search(word, it+1, self.root)
            else: 
                self.dp[it] = self.dp[it] or self.search(word, it+1, curr_trie.node[c])
        else: 
            self.dp[it] = self.dp[it] or False
        return self.dp[it]
        
            
    
class TrieNode():
    def __init__(self):
        self.node = {}
        self.is_end = False
