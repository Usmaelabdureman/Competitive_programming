class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        char_count = {'a': 0, 'b': 0, 'c': 0}
        left_ptr = 0
        substr_count = 0

        for right_ptr in range(len(s)):
            char_count[s[right_ptr]] += 1

            # Move the left pointer until all three characters are present in the substring
            while all(char_count.values()):
                char_count[s[left_ptr]] -= 1
                left_ptr += 1
            # Count substrings ending at the current right pointer position
            substr_count += left_ptr
        return substr_count
