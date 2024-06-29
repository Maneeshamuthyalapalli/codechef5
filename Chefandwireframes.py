T = int(input())
for _ in range(T):
    N, M, X = map(int, input().split())
    perimeter = 2 * N + 2 * M 
    total_cost = perimeter * X 
    print(total_cost)
