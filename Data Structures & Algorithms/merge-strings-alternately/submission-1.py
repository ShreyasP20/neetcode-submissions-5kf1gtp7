class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i =0 
        j = 0
        len_word1 = len(word1)
        len_word2 = len(word2)
        final_str = ""
        while i < len_word1 or j < len_word2:
            if i < len_word1:
                final_str += word1[i]
                i += 1
            if j < len_word2:
                final_str += word2[j]
                j += 1
        
        return final_str

            
