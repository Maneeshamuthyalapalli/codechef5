# cook your dish here
def determine_grade(attendence, marks):
    if attendence < 50:
        return "Z"
    elif marks < 50:
        return "F"
    else:
        return "A"
T = int(input())
for _ in range(T):
    attendence, marks = map(int, input().split())
    grade = determine_grade(attendence, marks) 
    print(grade)
        
        
