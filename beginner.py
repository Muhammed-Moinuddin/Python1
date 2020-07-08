a = int(input("Please enter first number: "))
b = int(input("Please enter Second number: "))
if a > b : print('{0} is the largest'.format(a))
else : print('{0} is the largest'.format(b))
#First input Positive or negative
if a > 0 :  print('{0} is Positive'.format(a)) 
else :  print('{0} is Negative'.format(a))  
#First input greater or smaller than 100
if a > 100 :  print('{0} is greater than 100'.format(a))
else : print ('{0} is smaller than 100'.format(a))
#First input even or odd
if a % 2 == 0 : print ('{0} is even'.format(a))
else : print ('{0} is odd'.format(a))
#First input divisible by 5 or not
if a % 5 == 0 : print ('{0} is divisible by 5'.format(a))
else : print ('{0} is not divisible by 5'.format(a))
#First input multiple of 7 or not
if a % 7 == 0 : print ('{0} is multiple of 7'.format(a))
else : print ('{0} is not multiple of 7'.format(a))
#Comparision of input
if a > b : print('{0} > {1}'.format(a,b))
elif a < b : print('{0} < {1}'.format(a,b))
else : print('{0} = {1}'.format(a,b))
#Program for grading
roll_num = int(input("Please enter roll number: "))
marks_1 = int(input("Please enter obtained marks for first subject : "))
marks_2 = int(input("Please enter obtained marks for second subject : "))
marks_3 = int(input("Please enter obtained marks for third subject : "))
total_marks = marks_1+marks_2+marks_3
avg = total_marks/3
print("Total marks:",total_marks)
print("Average:",avg)
print("RESULT:")
if avg >= 80 : print("Grade A+")
elif avg >= 70 : print("Grade A")
elif avg >= 60 : print("Grade B")
elif avg >= 50 : print("Grade c")
elif avg == 49 or avg <= 49 : print("Fail")
#Age convertor
age = int(input("Please enter Age in year: "))
months = age*12
print ('Age :{0} months old'.format(months))
days = age*365
print ('Age :{0} days old'.format(days))
#On Input providing corresponding Month
i = int(input("Please enter number of the month: "))
if i == 1 : print("January")
elif i == 2 : print("February")
elif i == 3 : print("March")
elif i == 4 : print("April")
elif i == 5 : print("May")
elif i == 6 : print("June")
elif i == 7 : print("July")
elif i == 8 : print("August")
elif i == 9 : print("September")
elif i == 10 : print("Octuber")
elif i == 11 : print("November")
elif i == 12 : print("December")
else : print("Invalid Number")
#On Single Value Input providing corresponding Month
i = int(input("Please enter number of the month: "))
if i == 1 : print("January")
elif i == 2 : print("February")
elif i == 3 : print("March")
elif i == 4 : print("April")
elif i == 5 : print("May")
elif i == 6 : print("June")
elif i == 7 : print("July")
elif i == 8 : print("August")
elif i == 9 : print("September")
else : print("Invalid Number")