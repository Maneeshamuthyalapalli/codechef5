T = int(input())
for _ in range(T):
    N, X, Y = map(int, input().split())
    total_size = X + 2 *  Y  
    if total_size <= N:
        print("YES")
    else:
        print("NO")
