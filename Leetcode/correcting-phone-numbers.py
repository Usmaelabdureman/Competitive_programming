

def PhoneCor(phone1,phone2):
    stack1=[]
    stack2=[]
    
    for i in range(len(phone1)):
        if phone1[i]!='#':
            stack1.append(phone1[i])
        elif phone1[i]=='#':
            stack1.pop()
    for i in range(len(phone2)):
        if phone2[i]!='#':
            stack2.append(phone2[i])
        elif phone2[i]=='#':
            stack2.pop()
    print(stack1)
    print(stack2)
    return  stack1==stack2

ph="09224##42568#8##5621"
ph2= "0924255621"

print(PhoneCor(ph,ph2))
