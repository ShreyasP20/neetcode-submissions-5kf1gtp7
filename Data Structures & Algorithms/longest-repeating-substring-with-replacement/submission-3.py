class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_rep = 0
        count_char = [0] * 26
        l = 0
        for r in range(len(s)):
            count_char[ord(s[r])-65] += 1
            while (r-l+1) - max(count_char) > k:
                count_char[ord(s[l])-65] -= 1
                l += 1
            
            longest_rep = max(longest_rep, (r-l+1))
        
        return longest_rep