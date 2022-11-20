# def Count(number):

#     count=0
#     if number < 1:
# 		return 0
    
# 	for i in range (2, number):
# 		if  number % i == 0:
#             count+=1
# 	return count
	
def CountPrime(number):
    if(number > 40): return number**2 - number + 41
    lst_prime=[2]
    checker=[True]*(number)
    for i in range(2,number):
        if checker[i] and i%2==1:
            lst_prime.append(i)
            for j in range(i,number,i):
                checker[j]=False
    return len(lst_prime)
        

# def Prime(n):
#     idx=1
#     lst=[]
#     for i in range(2,4):
#         if(n > i): lst.append(i)
#     while(True):
#         minus=6*idx-1
#         plus=6*idx+1
#         if minus>n:
#                 break
#         lst.append(minus)
#         if plus < n: lst.append(plus)    
#         idx+=1
#     return len(lst)

print(CountPrime(100))
