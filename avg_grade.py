# Write a program that will assign grades to the student according to the below scheme 
# If (avg_marks>=90) grade A
# If (avg_marks < 90 and avg_marks >= 80) grade B
# If (avg_marks < 80 and avg_marks >= 70) grade C
# If (avg_marks < 70 and avg_marks >= 60) grade D
# If (avg_marks<60) grade E

subject1_marks = 90
subject2_marks = 75
subject3_marks = 83
subject4_marks = 92
subject5_marks = 96

avg_marks = (subject1_marks+subject2_marks+ subject3_marks+subject4_marks+subject5_marks)/5

grade = "unknown"

if (avg_marks>=90):
    grade = "A"
elif (avg_marks < 90 and avg_marks >= 80):
    grade = "B"
elif (avg_marks < 80 and avg_marks >= 70):
    grade = "C"
elif (avg_marks < 70 and avg_marks >= 60):
    grade = "D"
elif (avg_marks<60):
    grade = "E"
    
print("subject1_marks : ", subject1_marks, 
       "\nsubject2_marks : ", subject2_marks,
       "\nsubject3_marks : ", subject3_marks,
       "\nsubject4_marks : ", subject4_marks,
       "\nsubject5_marks : ", subject5_marks )
print("********************") 
print("Final grade :", grade)
print ("*******************")
 
      