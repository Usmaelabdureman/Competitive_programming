class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_of_string=list(s)

        for i in range(0,len(list_of_string),2*k):
            list_of_string[i:i+k]=reversed(list_of_string[i:i+k])
        return ''.join(list_of_string)
