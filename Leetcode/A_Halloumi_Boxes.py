def can_sort_boxes(t, test_cases):
    results = []
    
    for i in range(t):
        n, k = test_cases[i][0]
        boxes = test_cases[i][1]
        
        sorted_boxes = sorted(boxes)
        if boxes == sorted_boxes:
            results.append("YES")
        elif k == 1 and boxes != sorted_boxes:
            results.append("NO")
        elif k >= n:
            results.append("YES")
        else:
            subarray = boxes[:k]
            subarray_sorted = sorted(subarray)
            
            if subarray == subarray_sorted:
                results.append("YES")
            else:
                results.append("NO")
    
    return results

# Example usage
t = int(input())
test_cases=[]

for _ in range(t):
    test_cases.append(int(input().split()))
can_sort_boxes()



