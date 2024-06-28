T = int(input().strip())
for _ in range(T):
    N, X, Y =map(int, input().strip().split())
    max_pages_chef_can_read = X *  Y    
    if max_pages_chef_can_read >= N:
        print("YES")
    else:
        print("NO")
