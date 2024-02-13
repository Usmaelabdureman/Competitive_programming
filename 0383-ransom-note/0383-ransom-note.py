class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counter = Counter(magazine)

        for char in ransomNote:
            counter[char] -= 1
            if counter[char] < 0:
                return False
        return True
            
            