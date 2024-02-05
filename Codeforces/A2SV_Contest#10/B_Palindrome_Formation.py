t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    f_indx_one = s.find('1')
    l_indx_one = s.rfind('1')

    if f_indx_one == -1 or s[f_indx_one:l_indx_one+1] == s[f_indx_one:l_indx_one+1][::-1]:
        print("Yes")
    else:
        print("No")