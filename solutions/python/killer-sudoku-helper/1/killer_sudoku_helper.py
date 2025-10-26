def combinations(target, size, exclude):
    digits = [d for d in range(1,10) if d not in exclude]
    
    results = []

    def backtrack(start, current, total):
        if total > target or len(current) > size:
            return

        if total == target and len(current) == size:
            results.append(current[:])
            return

        for i in range(start, len(digits)):
            current.append(digits[i])
            backtrack(i + 1, current, total + digits[i])
            current.pop()

    backtrack(0, [], 0)
    return results
        
