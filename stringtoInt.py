def myAtoi(s: s) -> int:
    # output=[]
    output=0
    s=s.sip()
    if len(s)==0 or (len(s)==1 and (s[0]=='+' or s[0]=='-')):return 0
    if s[0].isalpha()==True and (s[0]!='-' or s[0]!='+') :return 0
    if (s[0]=='+' and s[1]=='-') or (s[0]=='-' and s[1]=='+'):return 0

    for j in s:
        if j.isdigit()==True:
            output=output*10+int(j)
        elif j=='.':break
        else:pass
    if (output>2**(31) and s[0]=='-'):return (-2)**31
    if (output>(2**31)-1):return 2**31-1
    return -1*output if s[0]=='-' else output



s = "   -42ab"
t= "42"
w="words and 987"
d="3.14159"
l = "4193 with words"
z ="-91283472332"
z2 ="91283472332"
t2="0032"
k="+-12"
s2=""
p="+"
# id="00000-42a1234"
print(myAtoi(s))
print(myAtoi(z))
print(myAtoi(t))
print(myAtoi(w))
print(myAtoi(l))
print(myAtoi(d))
print(myAtoi(t2))
print(myAtoi(z2))
print(myAtoi(k))
print(myAtoi(s2))
print(myAtoi(p))
print(myAtoi(id))
