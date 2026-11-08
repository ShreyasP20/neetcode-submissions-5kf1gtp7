from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        n = len(s)
        char_freq = Counter(s)

        max_freq = max(char_freq.values())

        if max_freq > (n+1)//2: 
            return ""
        
        reorganized_string = [None] * n

        current_index = 0

        for character, frequency in char_freq.most_common():
            while frequency > 0:
                reorganized_string[current_index] = character
                frequency -= 1

                current_index += 2

                if current_index >= n:
                    current_index = 1
        
        return ''.join(reorganized_string)


