
def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i]<38:
            continue
        else:
            rem=grades[i]%5
            if rem>=3:grades[i]=(5-rem)+grades[i]
    return grades


  

gr=[4,38,57,45,67,73]
print(gradingStudents(gr))
# print(gr[3])