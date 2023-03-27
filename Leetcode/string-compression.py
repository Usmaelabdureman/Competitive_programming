class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        count = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i-1]:
                count += 1
            else:
                chars[index] = chars[i-1]
                index += 1
                if count == 1:
                    pass
                elif count <= 9:
                    chars[index] = str(count)
                    index += 1
                else:
                    count_str = str(count)
                    for c in count_str:
                        chars[index] = c
                        index += 1
                count = 1
        chars[index] = chars[-1]
        index += 1
        if count == 1:
            pass
        elif count <= 9:
            chars[index] = str(count)
            index += 1
        else:
            count_str = str(count)
            for c in count_str:
                chars[index] = c
                index += 1
        return index
