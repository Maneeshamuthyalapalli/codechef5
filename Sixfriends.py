T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    cost_double_rooms = 3 * X 
    cost_triple_rooms = 2 * Y             
    min_cost = min(cost_double_rooms, cost_triple_rooms)
    print(min_cost)
