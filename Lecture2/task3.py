quiz = int(input("Enter quiz score: "))
mid_term = int(input("Enter mid-term score: "))
final_score = int(input("Enter final score: "))

avg_score = float((quiz + mid_term + final_score) / 3)

if (avg_score >= 90):
    grade = 'A'
elif (70 <= avg_score < 90):
    grade = 'B'
elif (50 <= avg_score < 70):
    grade = 'C'
elif (avg_score < 50):
    grade = 'F'
else:
    print("Invalid")
    
print(avg_score)
print(grade)