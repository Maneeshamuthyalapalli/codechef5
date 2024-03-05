def check_withdrawals(N, K, amounts):
    result = []
    current_balance = K
    for amount in amounts:
        if amount <=current_balance:
            result.append(1)
            current_balance -= amount
        else:
            result.append(0)
    return ''.join(map(str, result))
T = int((input()))
for _ in range(T):
    N, K = map(int, input().split())
    amounts = list(map(int, input().split()))
    print(check_withdrawals(N, K, amounts))
