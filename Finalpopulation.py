T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    final_population = X - Y + Z 
    print(final_population)
