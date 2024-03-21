class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        
        houses.sort()
        heaters.sort()
        ans = 0

        for house in houses:
            # Find the closest heater to the current house using binary search
            closest_heater = bisect.bisect_left(heaters, house)

            # If the house is to the right of all heaters
            if closest_heater == len(heaters):
                radius = house - heaters[-1]

            # If the house is to the left of all heaters
            elif closest_heater == 0:
                radius = heaters[0] - house

            # If the house is between two heaters
            else:
                radius = min(heaters[closest_heater] - house, house - heaters[closest_heater - 1])

            ans = max(ans, radius)

        return ans