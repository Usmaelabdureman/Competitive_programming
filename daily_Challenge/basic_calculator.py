

def calculate(s: str) -> int:

    arr=[]
    output=[]
    precedence={'+':1,'-':"1",'*':2,'/':2,'^':3}

    def notPrior(i):
        try:
            a = precedence[i]
            b = precedence[arr[0]]
            return True if a <= b else False
        except KeyError:
            return False
    for i in s:
        if i==' ':
            continue
        if i.isalpha()==True:
            output.append(i)
        elif i=='(':
            arr.append(i)
        elif i==')':
            while(len(arr)!=0 and arr[0]!="(" ):
                a=arr.pop()
                output.append(a)
            if len(arr)!=0 and arr[0]!='(':
                    return -1
            # else:
                # arr.pop()
        else:
            while (len(arr)!=0 and notPrior(i)):
                output.append(arr.pop())
            arr.append(i)
        while len(arr)!=0:
            output.append(arr.pop())
       
    
s = "(110+50)*(2-4)"  
print(calculate(s))