class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = []
        longest_sub = 0

        for char in s:
            if char in seen_chars:
                duplicate_index = seen_chars.index(char)
                seen_chars = seen_chars[duplicate_index + 1:]

            seen_chars.append(char)
            longest_sub = max(longest_sub, len(seen_chars))

        return longest_sub