class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal=max(salary)
        min_sal=min(salary)
        salary.remove(max_sal)
        salary.remove(min_sal)
        return sum(salary)/len(salary)
        