print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
t=name1.upper().count('T')+name2.upper().count('T')
r=name1.upper().count('R')+name2.upper().count('R')
u=name1.upper().count('U')+name2.upper().count('U')
e=name1.upper().count('E')+name2.upper().count('E')
num1=t+r+u+e

l=name1.upper().count('L')+name2.upper().count('L')
o=name1.upper().count('O')+name2.upper().count('O')
v=name1.upper().count('V')+name2.upper().count('V')
es=name1.upper().count('E')+name2.upper().count('E')
num2=l+o+v+es

score=int(str(num1)+str(num2))

if score<10 or score>90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score>40 and score<50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

