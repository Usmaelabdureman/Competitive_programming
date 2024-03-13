import math
import signal
import sys
def largest_divisor_not_equal_to_itself(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return max(i, num // i)
    return num

def find_position_of_1(n):
    position = 1
    for i in range(2, n + 1):
        divisor = largest_divisor_not_equal_to_itself(i)
        position = position + (position - 1) // (divisor - 1)
        position %= n  # Ensure the position stays within array bounds
    return position

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        result = find_position_of_1(n)
        print(result)

def exit_gracefully(signum, frame):
    sys.exit(0)

if __name__ == "__main__":
    signal.signal(signal.SIGTERM, exit_gracefully)
    main()
