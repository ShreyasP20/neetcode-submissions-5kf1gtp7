class WordDictionary:

    def __init__(self):
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        d = self.trie
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
            
        d['/'] = '/'


    def search(self, word: str) -> bool:
        def dfs(curr, idx):
            if idx == len(word):
                return bool('/' in curr)
            
            letter = word[idx]
            if letter != '.':
                if letter not in curr: return False
                else: return dfs(curr[letter], idx+1)
            else:
                return any(dfs(curr[letter], idx+1) for letter in curr if letter != '/')

        return dfs(self.trie, 0) 