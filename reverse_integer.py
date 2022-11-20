class Solution:
    def reverse(self, x: int) -> int:
        if x >=-2147483648 and x<=2147483647:
            lst=[]
            if x<0:
                x=abs(x)
                x=str(x)
                for i in x:
                    lst.append(i)
                res=-1*int(''.join(lst[::-1]))
                if res<-2147483648:
                    return 0
                return res
            else:
                x=str(x)
                for i in x:
                    lst.append(i)
                res=int(''.join(lst[::-1]))
                if res>2147483647:
                    return 0
                return res
        else:
            return 0

tr=Solution()
print(tr.reverse(987576))