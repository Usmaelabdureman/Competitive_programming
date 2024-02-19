from math import gcd
from typing import Tuple
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:


        IntPair = Tuple[int,int] # used for 

        def slope(a: IntPair, b: IntPair) -> IntPair:


            changeInX = b[0] - a[0]
 
            # normalize undefined slopes to (1, 0)
            if changeInX == 0:
                return (1, 0)
        
            # normalize to left-to-right
            if changeInX < 0:
                a, b = b, a
                changeInX = b[0] - a[0]
        
            changeInY = b[1] - a[1]
            # Normalize by greatest common divisor.
            # math.gcd only works on positive numbers.
            gcd_ = gcd(abs(changeInY), changeInX)
            return (
                changeInY // gcd_,
                changeInX // gcd_,
            )
        if len(points) < 3:
            return len(points)
 
        # Note that every line we find will have at least 2 points.
        # There will be at least one line because len(points) >= 3.
        # Therefore, it's safe to initialize to 0.
        max_val = 0
    
        for a_index in range(0, len(points) - 1):
            # All lines in this iteration go through point a.
            # Note that lines a-b and a-c cannot be parallel.
            # Therefore, if lines a-b and a-c have the same slope, they're the same
            # line.
            a = tuple(points[a_index])
            # Fresh lines already have a, so default=1
            slope_counts: DefaultDict[IntPair, int] = defaultdict(lambda: 1)
    
            for b_index in range(a_index + 1, len(points)):
                b = tuple(points[b_index])
                slope_counts[slope(a, b)] += 1
    
            max_val = max(
                max_val,
                max(slope_counts.values()),
            )
    
        return max_val