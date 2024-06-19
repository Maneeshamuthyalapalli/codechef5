# cook your dish here
def check_subscription(lecture_durations):
    results = []
    for duration in lecture_durations:
        if duration > 30:
            results.append("YES")
        else:
            results.append("NO")
    return results
T = int(input().strip())
lecture_durations = [] 
for _ in range(T):
    X = int(input().strip())
    lecture_durations.append(X)
results = check_subscription(lecture_durations)
for result in results:
    print(result)
