student_score=input("Enter the score seperated by commas")
scores=[int(score) for score in student_score.split(",")]
grades=[
    "A" if score>=90 else
    "B" if score>=80 else
    "C" if score>=70 else
    "D" if score>=60 else
    "F"
    for score in scores 
]
passing_students=[score for score in scores if score>=60]
failing_students=[score for score in scores if score<60]
print("---Student grades---")
for i,(score,grade) in enumerate(zip(scores,grades),start=1):
    print(f"Student {i} : Score={score} , Grade={grade}")
print("\n----passing students and failing students----")
print("passing students : ",passing_students)
print("failing student : ",failing_students)

