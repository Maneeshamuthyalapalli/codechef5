def weekly_food_cost(X, Y):
    mess_cost = X * 6
    total_cost = mess_cost + Y 
    return total_cost
X, Y  = map(int, input().split())
print(weekly_food_cost(X, Y))
