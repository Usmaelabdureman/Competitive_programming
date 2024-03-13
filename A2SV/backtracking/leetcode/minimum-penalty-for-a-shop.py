class Solution:
    def bestClosingTime(self, customers: str) -> int:

        n = len(customers)
        satisf = [0] * (n + 1)

        for i, cust in enumerate(customers):
            satisf[i + 1] = satisf[i] + int(cust == 'Y')

        ans = 0
        cost = float("inf")

        for cur_time in range(n + 1):
            rem_cust = cur_time - satisf[cur_time] + satisf[-1] - satisf[cur_time]
            if cost > rem_cust:
                ans, cost = cur_time, rem_cust

        return ans