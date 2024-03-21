class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        maxRadius = 0

        i = 0  # Index for houses
        j = 0  
        while i < len(houses):
            while j < len(heaters) - 1 and abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1]):
                j += 1

            maxRadius = max(maxRadius, abs(houses[i] - heaters[j]))

            i += 1

        return maxRadius