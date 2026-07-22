class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def validate_cap(cap):
            currcap = 0
            req_days = 1
            for i in weights:
                if currcap + i > cap:
                    currcap = i
                    req_days += 1
                else:
                    currcap += i
        
            return req_days <= days

        l, r = max(weights), sum(weights)

        while l < r:
            cap = (l+r)//2
            if validate_cap(cap):
                r = cap
            else:
                l = cap + 1
        
        return l


