class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
            ans = []
            l1_pointer = 0
            l2_pointer = 0

            while l1_pointer < len(firstList) and l2_pointer < len(secondList):

                start1,end1 = firstList[l1_pointer]
                start2,end2 = secondList[l2_pointer]

                if start1 <= end2 and start2 <= end1:
                    ans.append([max(start1,start2), min(end1,end2)])
                if end1 <= end2:
                    l1_pointer += 1
                else:
                    l2_pointer += 1
            return ans
                
                

