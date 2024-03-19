# Function to calculate the minimum time after which all dishes can be at Petya's home
def min_delivery_time(num_dishes, courier_times, pickup_times):
    courier_times.sort()  # Sort the courier delivery times
    
    # Calculate suffix sums for pickup times
    suffix_sum = sum(pickup_times)
    min_time = suffix_sum  
    
    for i in range(num_dishes):
        prefix_time = courier_times[i]  # Prefix time is the maximum of courier delivery time
        
        suffix_sum -= pickup_times[i]  # Update suffix sum by subtracting current pickup time
        total_time = max(prefix_time, suffix_sum)  # Calculate total time
        
        min_time = min(min_time, total_time)  # Update minimum time if necessary
    
    return min_time


num_test_cases = int(input())

# Iterate through each test case
for _ in range(num_test_cases):
    num_dishes = int(input())  # Number of dishes for this test case
    courier_times = list(map(int, input().split()))  # Courier delivery times
    pickup_times = list(map(int, input().split()))  # Pickup times
    
    # Calculate and print the minimum time after which all dishes can be at Petya's home
    print(min_delivery_time(num_dishes, courier_times, pickup_times))
