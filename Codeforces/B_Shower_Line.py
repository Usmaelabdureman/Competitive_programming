"""
Many students live in a dormitory. A dormitory is a whole new world of funny amusements and possibilities but it does have its drawbacks.

There is only one shower and there are multiple students who wish to have a shower in the morning. That's why every morning there is a line of five people in front of the dormitory shower door. As soon as the shower opens, the first person from the line enters the shower. After a while the first person leaves the shower and the next person enters the shower. The process continues until everybody in the line has a shower.

Having a shower takes some time, so the students in the line talk as they wait. At each moment of time the students talk in pairs: the (2i - 1)-th man in the line (for the current moment) talks with the (2i)-th one.

Let's look at this process in more detail. Let's number the people from 1 to 5. Let's assume that the line initially looks as 23154 (person number 2 stands at the beginning of the line). Then, before the shower opens, 2 talks with 3, 1 talks with 5, 4 doesn't talk with anyone. Then 2 enters the shower. While 2 has a shower, 3 and 1 talk, 5 and 4 talk too. Then, 3 enters the shower. While 3 has a shower, 1 and 5 talk, 4 doesn't talk to anyone. Then 1 enters the shower and while he is there, 5 and 4 talk. Then 5 enters the shower, and then 4 enters the shower.

We know that if students i and j talk, then the i-th student's happiness increases by gij and the j-th student's happiness increases by gji. Your task is to find such initial order of students in the line that the total happiness of all students will be maximum in the end. Please note that some pair of students may have a talk several times. In the example above students 1 and 5 talk while they wait for the shower to open and while 3 has a shower.

Input
The input consists of five lines, each line contains five space-separated integers: the j-th number in the i-th line shows gij (0 ≤ gij ≤ 105). It is guaranteed that gii = 0 for all i.

Assume that the students are numbered from 1 to 5.

Output
Print a single integer — the maximum possible total happiness of the students.

Examples
inputCopy
0 0 0 0 9
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
7 0 0 0 0
outputCopy
32
inputCopy
0 43 21 18 2
3 0 21 11 65
5 2 0 1 4
54 62 12 0 99
87 64 81 33 0
outputCopy
620
Note
In the first sample, the optimal arrangement of the line is 23154. In this case, the total happiness equals:

(g23 + g32 + g15 + g51) + (g13 + g31 + g54 + g45) + (g15 + g51) + (g54 + g45) = 32
    """

def main():
    while True:
        try:
            arr = []
            arr.append(list(map(int, input().split())))
            max_val = 0
            q = [1, 2, 3, 4, 5]
            for i in range(1, 5):
                arr.append(list(map(int, input().split())))
            
            while True:
                tmp = q[:]
                lol = 0
                while tmp:
                    for i in range(0, len(tmp)-1, 2):
                        lol += arr[tmp[i]-1][tmp[i+1]-1] + arr[tmp[i+1]-1][tmp[i]-1]
                    del tmp[0]
                
                if lol > max_val:
                    max_val = lol

                if not next_permutation(q):
                    break

            print(max_val)
        
        except EOFError:
            break

def next_permutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    
    if i >= 0:
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1:] = arr[i + 1:][::-1]
    return i >= 0
        

if __name__ == "__main__":
    main()
