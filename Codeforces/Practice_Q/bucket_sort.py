from math import ceil
def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key
        
    return bucket

def bucket_sort(arr, n):
    # Sort a large set of floating point numbers which are uniformly distributed across the range. 
    
    # write your code here
    max_val = max(arr)
    min_val = min(arr)
    
    bucket_size = max_val - min_val + 1
    buckets = [[] for _ in range((n + 1))]
    
    for i in range(n):
        bucket_index = int(n*(arr[i] - min_val) // bucket_size)
        
        buckets[bucket_index].append(arr[i])
        
    print("bucket size",ceil(bucket_size))
    print("buckets  ,",buckets)
    
    ans = []
    for bucket in buckets:
        insertion_sort(bucket)
        ans.extend(bucket)
    return ans
    
    



# Test cases
def test():
    # Test case 1
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    assert bucket_sort(arr, len(arr)) == [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897], "Test case 1 failed"
    
    # Test case 2
    arr = [0.5, 0.1, 0.9, 0.3, 0.7]
    assert bucket_sort(arr, len(arr)) == [0.1, 0.3, 0.5, 0.7, 0.9], "Test case 2 failed"
    
     # Test case 3
    arr = [3.9, 0.9, 1.9, 5.9, 2.9, 4.9]
    assert bucket_sort(arr, len(arr)) == [0.9, 1.9, 2.9, 3.9, 4.9, 5.9], "Test case 3 failed"
    
    print("All test cases passed!")

# Run test cases
test()
