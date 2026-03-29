class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs or len(strs) <= 1:
            return [strs]
        
        sorted_strs = dict()
        for i in strs:
            key = "".join(sorted(i))
            if key not in sorted_strs.keys():
                sorted_strs[key] = [i]
            else:
                sorted_strs[key].append(i)
        

        group_anagrams = []
        for i in sorted_strs.keys():
            group_anagrams.append(sorted_strs[i])
        
        return group_anagrams