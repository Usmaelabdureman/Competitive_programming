class Solution:
    def reverseWords(self, s: str) -> str:
        last_space_index = -1
        ch_array = list(s)
        length = len(s)

        for str_index in range(length + 1):
            if str_index == length or ch_array[str_index] == ' ':
                start_index = last_space_index + 1
                end_index = str_index - 1

                while start_index < end_index:
                    ch_array[start_index], ch_array[end_index] = ch_array[end_index], ch_array[start_index]
                    start_index += 1
                    end_index -= 1

                last_space_index = str_index

        return ''.join(ch_array)