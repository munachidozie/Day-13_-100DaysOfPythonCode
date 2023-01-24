print ("== Exam Grade Calculator ==")
print ()
exam_name = input ("Name of Exam:  ")
print (exam_name)
print ()
max_score = float(input ("Input the maximum score:  "))
print ("the total score is", max_score)
print ()
your_score = float(input("Input your score:  "))
print ("Your score is", your_score)
print ()
percent_score = round(float((your_score / max_score )* 100))

if percent_score <= 39:
  print ("You got", percent_score, "% which is an F")
elif 40 >= percent_score <= 44:
  print ("You got", percent_score, "% which is an E")
elif 45 >= percent_score <= 49:
  print ("You got", percent_score, "% which is a D")
elif 50 >= percent_score <= 59:
  print ("You got", percent_score, "% which is a C")
elif 60 >= percent_score <= 69:
  print ("You got", percent_score, "% which is a B")
elif 70 >= percent_score <= 100:
  print ("You got", percent_score, "% which is a B")
else:
  print ("Input correct score")