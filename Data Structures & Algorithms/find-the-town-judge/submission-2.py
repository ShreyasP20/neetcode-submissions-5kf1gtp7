class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted_count = [0] * (n)
        truster_count = [0] * (n)

        for trust_pair in trust:
            trusted_count[trust_pair[1] - 1] += 1
            truster_count[trust_pair[0] - 1] += 1


        for i in range(n):
            if trusted_count[i] == n-1 and truster_count[i] == 0:
                return i+1
        
        return -1