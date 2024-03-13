t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    skills = list(map(int, input().split()))
    
    skills.sort()  # Sort the skills in ascending order
    
    teams = 0
    current_team = 0
    
    for skill in skills:
        current_team += 1
        
        if skill * current_team >= x:
            teams += 1
            current_team = 0
    
    print(teams)
