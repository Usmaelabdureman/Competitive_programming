# def Count(number):

#     count=0
#     if number < 1:
# 		return 0
    
# 	for i in range (2, number):
# 		if  number % i == 0:
#             count+=1
# 	return count
	
def CountPrime(number):
    lst_prime=[2]
    checker=[True]*(number)
    for i in range(2,number):
        if checker[i] and i%2==1:
            lst_prime.append(i)
            for j in range(i,number,i):
                checker[j]=False
    return len(lst_prime)
