T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    points_to_win_Alice = 7 - A 
    points_to_win_Bob = 7 - B 
    min_points_further_scored = min(points_to_win_Alice, points_to_win_Bob)
    print(min_points_further_scored)
