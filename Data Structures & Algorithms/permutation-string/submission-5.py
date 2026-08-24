import collections 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1) - 1
        while r < len(s2):
            # print("S:",s2[l:r+1])
            # print("Counter_S1:",Counter(s1))
            # print("Counter_S2:",Counter(s2[l:r+1]))
            if Counter(s1) == Counter(s2[l:r+1]):
                return True
            
            l += 1
            r += 1
        
        return False