class Solution:
    def trap(self, height: List[int]) -> int:
        l_wl = r_wl = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        for i in range(n):
            j = -i - 1
            max_left[i] = l_wl
            max_right[j] = r_wl
            l_wl = max(l_wl, height[i])
            r_wl = max(r_wl , height[j])

        
        summ = 0
        print(max_left)
        print(max_right)
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])
        

        return summ