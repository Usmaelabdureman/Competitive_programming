class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        rev_1 = version1.split('.')
        rev_2= version2.split('.')
        
        for i in range(max(len(rev_1), len(rev_2))):
            rev1 = int(rev_1[i]) if i < len(rev_1) else 0
            rev2 = int(rev_2[i]) if i < len(rev_2) else 0
            
            if rev1 < rev2:
                return -1
            elif rev1 > rev2:
                return 1
        
        return 0
