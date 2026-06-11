class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            if i[len(i) - 1] < target:
                continue
            l = 0
            r = len(i) - 1
            while l <= r:
                mid = (l+r)//2
                if i[mid] == target:
                    return True
                elif i[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            
        return False
