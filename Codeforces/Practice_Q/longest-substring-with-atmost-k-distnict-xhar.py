
def LongestSubstringWithAtmostKDistinctChar(s, k):
    if not s or k < 0:
        return 0
    if k == 0:
        return 0
    if k == 1:
        return 1
    if k >= len(s):
        return len(s)
    
    left = 0
    right = 0
    max_len = 0
    char_count = {}
    while right < len(s):
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
        right += 1
    return max_len

test = "eceba"
k = 3
print(LongestSubstringWithAtmostKDistinctChar(test, k))  # Output: 3