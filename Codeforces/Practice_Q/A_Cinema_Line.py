
def lemonadeChange(bills):
    five = 0
    ten = 0
    
    for bill in bills:
        if bill == 25:
            five += 1
        elif bill == 50:
            if not five: return False
            five -= 1
            ten += 1
        else:
            if ten and five:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True

num_people = int(input())
bill_note = list(map(int,input().split()))

if lemonadeChange(bill_note):
    print("YES")
else:
    print("NO")
