import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        element_heap = []

        for i in nums:
            heapq.heappush(element_heap, i)

            if len(element_heap) > k:
                heapq.heappop(element_heap)
        
        return heapq.heappop(element_heap)