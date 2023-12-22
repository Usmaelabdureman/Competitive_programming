class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)

        for i in range(n):
            image[i].reverse()
        
        for i in range(n):
            for j in range(n):
                if image[i][j] == 1:
                    image[i][j] =0
                else:
                    image[i][j]=1
        return image


        
