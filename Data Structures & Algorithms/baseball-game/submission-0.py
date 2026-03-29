class Solution:
    def calPoints(self, operations: List[str]) -> int:
        points = list()
        for i in operations:
            if i != '+' and i != 'C' and i != 'D':
                points.append(int(i))
            elif i == '+':
                points.append(points[-1] + points[-2])
            elif i == 'C':
                points.pop()
            elif i == 'D':
                points.append(points[-1]*2)
        
        return sum(points)