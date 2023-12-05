class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_steps = 0
        can_water = capacity # initialize the capacity of the watering_can 
        for i in range(len(plants)):
            if plants[i] <= can_water:  # Check if its possible to water the plant if so go step by 1.
                total_steps +=1 
                 # Check if the plant needs more water than the can has
            if plants[i] > can_water:
                can_water = capacity  # Refill the can
                total_steps += 2 * (i)+1  # Go back to the river and return to the plant
            can_water -= plants[i]  # Water the current plant
        return total_steps
