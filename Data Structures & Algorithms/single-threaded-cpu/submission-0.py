import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        solution = []
        task_heap = []
        i = 0
        t = 0
        n = len(tasks)
        for i2,task in enumerate(tasks):
            task.append(i2)

        tasks.sort()
        
        while task_heap or i < n:
            if not task_heap:
                t = max(t, tasks[i][0])
            
            while i < n and tasks[i][0] <= t:
                heapq.heappush(task_heap, (tasks[i][1], tasks[i][2]))
                i += 1

            processing_time, task_index = heapq.heappop(task_heap)
            solution.append(task_index)
            t += processing_time
    

        return solution
