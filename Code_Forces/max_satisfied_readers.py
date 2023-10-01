def max_satisfied_readers(n, k, a):
    # Sort the books in descending order of demand
    books = sorted(range(k), key=lambda i: -a[i])
    # Initialize set of satisfied readers
    satisfied = set()
    # Iterate through the books and assign them to readers
    for i in books:
        # Find the reader with the highest remaining demand
        best_reader = max(range(n), key=lambda j: a[i] if j not in satisfied and a[i] <= a[j] else -1)
        # Assign the book to the best reader
        if best_reader not in satisfied:
            satisfied.add(best_reader)
    # Return the number of satisfied readers
    return len(satisfied)
