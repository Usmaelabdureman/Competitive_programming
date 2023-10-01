class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=set("aeiouAEIOU")
        a=s[:len(s)//2]
        b=s[len(s)//2:]
        count1=0
        count2=0
        for i in a:
            if i in vowels:
                count1+=1
        for i in b:
            if i in vowels:
                count2+=1
        return True if count1==count2 else False
