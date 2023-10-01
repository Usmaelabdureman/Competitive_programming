function maximumRequests(n: number, requests: number[][]): number {
    let answer = 0;

    function maxRequest(indegree: number[], index: number, count: number): void {
        if (index === requests.length) {
            // Check if all buildings have an in-degree of 0.
            for (let i = 0; i < n; i++) {
                if (indegree[i] !== 0) {
                    return;
                }
            }

            answer = Math.max(answer, count);
            return;
        }

        // Consider this request, increment and decrement for the buildings involved.
        indegree[requests[index][0]]--;
        indegree[requests[index][1]]++;
        // Move on to the next request and also increment the count of requests.
        maxRequest(indegree, index + 1, count + 1);
        // Backtrack to the previous values to move back to the original state before the second recursion.
        indegree[requests[index][0]]++;
        indegree[requests[index][1]]--;

        // Ignore this request and move on to the next request without incrementing the count.
        maxRequest(indegree, index + 1, count);
    }

    const indegree: number[] = new Array(n).fill(0);
    maxRequest(indegree, 0, 0);

    return answer;
}
