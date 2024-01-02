class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        ans=0
        skill.sort()
        left =0
        right=len(skill)-1
        target=skill[right]+skill[left]
        while left <right:
            if skill[left]+skill[right] == target:
                ans+=(skill[left]*skill[right])
                left+=1
                right-=1
            else:
                return -1
        return ans



        