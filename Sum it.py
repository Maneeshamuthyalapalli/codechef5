def is_sum_correct(test_cases):
    results = []
    for A, B, C in test_cases:
        if A + B == C:
            results.append("YES")
        else:
            results.append("NO")
    return results 
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]
results = is_sum_correct(test_cases)
for result in results:
    print(result)
