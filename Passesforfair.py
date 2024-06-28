T = int(input().strip())
for _ in range(T):
    N, K = map(int, input().strip().split())
    passes_needed = N + 1 
    if K >= passes_needed:
        print("YES")
    else:
        print("NO")
