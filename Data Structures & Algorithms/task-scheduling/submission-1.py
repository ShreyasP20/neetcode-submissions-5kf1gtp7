from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_frequency = max(task_counts.values())
        tasks_w_max_freq = 0
        for i in task_counts.values():       
            if i == max_frequency:
                tasks_w_max_freq += 1
        number_of_tasks = len(tasks)
        return max(number_of_tasks, int((max_frequency - 1) * (n + 1) + tasks_w_max_freq))