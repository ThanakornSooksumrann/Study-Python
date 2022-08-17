# Program name : Exam9_6.py
from random import randint

def Read_Scores():
    Score = []
    Done = True
    count = 1
    while Done:
        score = int(input(f"Enter score #{count} (-1 to exit): "))
        if score >= 0 and score <= 100:
            Score += (score,)
            count += 1
        elif score == -1:
           break
    count -= 1
    return(Score)

def Check_Grade(Scores):
    Grades = []
    for score in Scores:
        grade = ""
        if score >= 80:
            grade = "A"
        elif score >= 70:
            grade = "B"
        elif score >= 60:
            grade = "C"
        elif score >= 50:
            grade = "D"
        else:
            grade = "F"
        Grades += (grade,)
    return(Grades)

def Report_Grades(Scores, Grades):
    Max = len(Scores)
    print("="*24)
    print("| No. | Score | Grade |")
    print("="*24)
    for n in range(Max):
        print(f"| %2d | %3d | %s |"%(n+1, Scores[n], Grades[n]))
    print("="*24)

# main program
Scores = Read_Scores()
Grades = Check_Grade(Scores)
Report_Grades(Scores, Grades)

print(f"End Program.")
