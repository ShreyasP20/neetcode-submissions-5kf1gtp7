import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        distance_heap = []

        for i in points:
            x, y = i
            heapq.heappush(distance_heap, (-(x**2 + y**2), x, y))

            if len(distance_heap) > k:
                heapq.heappop(distance_heap)


        closest_points = [[x,y] for _,x,y in distance_heap]
        return closest_points
