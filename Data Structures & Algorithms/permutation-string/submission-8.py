import collections 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        s1_counter = Counter(s1)
        while r < len(s2):
            if s1_counter == Counter(s2[l:r+1]):
                return True
            
            l += 1
            r += 1
        
        return False