class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # for i in range(n):
        #     for j in range(i+1 ,n):
        #         if (numbers[i] + numbers[j]) == target:
        #             return [i+1, j+1]
        l,r = 0, n-1

        while l < r:
            h_target = numbers[l] + numbers[r]
            print(h_target)
            if target == h_target:
                return [l+1, r+1]
            elif h_target > target:
                r -= 1
            elif h_target < target:
                l += 1 

        return [0, 0]

