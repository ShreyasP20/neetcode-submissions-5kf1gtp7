import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        distance_heap = []
        heapq.heapify(distance_heap)

        for i in points:
            x, y = i
            heapq.heappush(distance_heap, (x**2 + y**2, x, y))

        for i in range(k):
            distance, x, y = heapq.heappop(distance_heap)
            closest_points.append([x, y])


        return closest_points
