class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = dict()
        for i in nums:
            if i in freqMap.keys():
                freqMap[i] += 1 
            else:
                freqMap[i] = 1
        
        sorted_items = sorted(freqMap.items(), key=lambda x:x[1], reverse=True)
        k_elements = []
        for i in range(k):
            k_elements.append(sorted_items[i][0])
        

        return k_elements