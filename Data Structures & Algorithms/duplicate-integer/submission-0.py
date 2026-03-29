class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNumbers = []
        for i in nums:
            if i not in seenNumbers:
                seenNumbers.append(i)
            else:
                return True

        return False