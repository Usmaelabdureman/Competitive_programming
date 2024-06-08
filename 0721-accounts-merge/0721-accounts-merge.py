class UnionFind:
    def __init__(self, sz):
        self.parent = list(range(sz))
        self.size = [1] * sz

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        rep_a = self.find(a)
        rep_b = self.find(b)

        if rep_a == rep_b:
            return

        if self.size[rep_a] >= self.size[rep_b]:
            self.size[rep_a] += self.size[rep_b]
            self.parent[rep_b] = rep_a
        else:
            self.size[rep_b] += self.size[rep_a]
            self.parent[rep_a] = rep_b


class Solution:
    def accountsMerge(self, accountList):
        account_len = len(accountList)
        dsu = UnionFind(account_len)

        email_group = {}

        for i in range(account_len):
            account_size = len(accountList[i])

            for j in range(1, account_size):
                email = accountList[i][j]
                account_name = accountList[i][0]

                if email not in email_group:
                    email_group[email] = i
                else:
                    dsu.union(i, email_group[email])

        components = {}
        for email in email_group:
            group = email_group[email]
            group_rep = dsu.find(group)

            if group_rep not in components:
                components[group_rep] = []

            components[group_rep].append(email)

        merged_accounts = []
        for group in components:
            component = sorted(components[group])
            component.insert(0, accountList[group][0])
            merged_accounts.append(component)

        return merged_accounts


