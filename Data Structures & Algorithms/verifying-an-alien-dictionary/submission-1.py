class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_to_position = {char:position for position, char in enumerate(order)}
        found_difference = None
        for i in range(1, len(words)):
            previous_word = words[i-1]
            current_word = words[i]

            min_length = min(len(previous_word), len(current_word))

            for j in range(min_length):
                previous_word_alpha = previous_word[j]
                current_word_alpha = current_word[j]
                previous_word_alpha_value = char_to_position[previous_word_alpha]
                current_word_alpha_value = char_to_position[current_word_alpha]

                if previous_word_alpha_value > current_word_alpha_value:
                    return False
                
                if previous_word_alpha_value < current_word_alpha_value:
                    found_difference = True
                    break

        if not found_difference and len(previous_word) > len(current_word):
            return False
        return True



