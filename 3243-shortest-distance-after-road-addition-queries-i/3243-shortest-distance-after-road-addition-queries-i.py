class Solution:

    # Helper function to perform BFS and find the number of edges in the shortest path from node 0 to node n-1
    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        visited = [False] * n
        node_queue = deque()

        # Start BFS from node 0
        node_queue.append(0)
        visited[0] = True

        # Track the number of nodes in the current layer and the next layer
        current_layer_node_count = 1
        next_layer_node_count = 0
        # Initialize layers explored count
        layers_explored = 0

        # Perform BFS until the queue is empty
        while node_queue:
            # Process nodes in the current layer
            for _ in range(current_layer_node_count):
                current_node = node_queue.popleft()

                # Check if we reached the destination node
                if current_node == n - 1:
                    return layers_explored  # Return the number of edges in the shortest path

                # Explore all adjacent nodes
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    node_queue.append(
                        neighbor
                    )  # Add neighbor to the queue for exploration
                    next_layer_node_count += (
                        1  # Increment the count of nodes in the next layer
                    )
                    visited[neighbor] = True

            # Move to the next layer
            current_layer_node_count = next_layer_node_count
            next_layer_node_count = 0  # Reset next layer count
            layers_explored += 1  # Increment the layer count after processing the current layer

        return -1  # Algorithm will never reach this point

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        # Initialize the graph with edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        # Process each query to add new roads
        for road in queries:
            u, v = road
            adj_list[u].append(v)  # Add road from u to v
            # Perform BFS to find the shortest path after adding the new road
            answer.append(self.bfs(n, adj_list))

        return answer
