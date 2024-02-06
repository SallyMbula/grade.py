first_score = float(input("Enter First Score: "))
second_score = float(input("Enter Second Score: "))
third_score = float(input("Enter Third Score: "))

#calculate average score
average_score = (first_score + second_score + third_score) / 3

#Assign Grade
if average_score >= 70 and average_score <= 100:
  grade = "A"
elif average_score >= 60:
  grade = "B"
elif average_score >= 50:
  grade = "C"
elif average_score >= 40:
  grade = "D"
else:
  grade = "Fail"
#Print Grade
print("Your grade is: " + grade)
