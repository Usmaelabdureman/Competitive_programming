from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1
        
        # Possible mutation directions
        directions = ['A', 'C', 'G', 'T']
        
        queue = deque([(startGene, 0)])  # Start with the initial gene and 0 mutations
        visited = set()  # To avoid revisiting the same gene
        
        while queue:
            gene, mutations = queue.popleft()
            
            if gene == endGene:
                return mutations
            
            for i in range(len(gene)):
                for direction in directions:
                    new_gene = gene[:i] + direction + gene[i+1:]
                    if new_gene in bank_set and new_gene not in visited:
                        visited.add(new_gene)
                        queue.append((new_gene, mutations + 1))
        
        return -1  # No valid mutation sequence found