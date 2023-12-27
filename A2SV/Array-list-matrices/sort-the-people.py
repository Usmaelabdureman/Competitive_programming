class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
            n=len(names)
            # Using Bubble sort
            for i in range(n):
                for j in range(n-i-1):
                    if heights[j]<heights[j+1]:
                        heights[j],heights[j+1]=heights[j+1],heights[j]
                        names[j],names[j+1]=names[j+1],names[j]
            
            # Using selection sort
            for i in range(n):
                min_index = i
                for j in range(i + 1, n):
                    if heights[j] >  heights[min_index]:
                        min_index = j
                heights[i], heights[min_index] = heights[min_index], heights[i]
                names[i], names[min_index] = names[min_index], names[i]

            # Insertion Sort
            for i in range(1, n):
                key_height = heights[i]
                key_name = names[i]
                j = i - 1
                while j >= 0 and key_height > heights[j]:
                    heights[j + 1] = heights[j]
                    names[j + 1] = names[j]
                    j -= 1
                heights[j + 1] = key_height
                names[j + 1] = key_name


            # Counting Sort
            min_height=min(heights)
            range_height = max(heights) - min(heights) + 1
            count = [0] * range_height
            output_heights = [0] * n
            output_names = [''] * n

            for i in range(n):
                count[heights[i] - min_height] += 1

            for i in range(1, range_height):
                count[i] += count[i - 1]

            for i in range(n - 1, -1, -1):
                index = heights[i] - min_height
                output_heights[count[index] - 1] = heights[i]
                output_names[count[index] - 1] = names[i]
                count[index] -= 1

            for i in range(n):
                heights[i] = output_heights[n - i - 1]
                names[i] = output_names[n - i - 1]
            return names