def minimum_attacks(t, test_cases):
    for _ in range(t):
        n = test_cases[_][0]
        hordes = test_cases[_][1]

        attacks = 0
        x = 0
        left = 0
        right = n - 1

        while left <= right:
            if hordes[left] <= x:
                x += right-left
                
                left += 1
            elif hordes[right] <= x:
                x += right+left
                right -= 1
            else:
                x += 1
                attacks += 1
        print(attacks)
        

# Example usage
test_cases = [
    (4, [1, 3, 1, 1]),
    (4, [1, 2, 1, 1]),
    (6, [3, 2, 1, 5, 2, 4]),
    (2, [1, 6])
]

minimum_attacks(4, test_cases)
