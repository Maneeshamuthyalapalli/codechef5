def can_enter_token(x):
    if x == 6:
        return "YES"
    else:
        return "NO"
t = int(input())
for _ in range (t):
    x = int(input())
    result = can_enter_token(x)
    print(result)
