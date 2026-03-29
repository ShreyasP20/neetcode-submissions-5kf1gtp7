class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:    
        if not strs:
            return ""

        min_length = float('inf')

        for i in strs:
            if min_length > len(i):
                min_length = len(i)
        
        for i in range(min_length):
            for word in strs:
                if word[i] != strs[0][i]:
                    return strs[0][:i]

        
        return strs[0][:min_length]