import math

def max_rest_days(t, test_cases):
    for _ in range(t):
        n, P, l, t = test_cases[_]
        
        total_lesson_points = n * l
        total_tasks = n // 7 * 2 + min(n % 7, 2)
        total_task_points = total_tasks * t
        
        total_points = total_lesson_points + total_task_points
        
        if total_points < P:
            print(0)
            continue
        
        days_required = math.ceil(P / (l + t))
        rest_days = n - days_required
        
        print(max(rest_days, 0))

# Example test cases
t = int(input().strip())
test_cases = []

# Read each test case
for _ in range(t):
    n, P, l, t = map(int, input().strip().split())
    test_cases.append((n, P, l, t))

max_rest_days(t, test_cases)