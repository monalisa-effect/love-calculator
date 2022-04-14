# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1=name1.lower()
#name2 = name2.lower()
love = 0
true = 0
l = name1.count('l')
l2= name2.count('l')
o = name1.count('o')
o2= name2.count('o')
v = name1.count('v')
v2= name2.count('v')
e= name1.count('e')
e2= name2.count('e')

t = name1.count('t')
t2= name2.count('t')
r = name1.count('r')
r2= name2.count('r')
u = name1.count('u')
u2= name2.count('u')


if l >=1 or o>=1 or v>=1 or e>=1:
  love = love + o+l+v+e+l2+o2+v2+e2

if t >=1 or r>=1 or u>=1 or e>=1:
  true = true + t+r+u+e+t2+r2+u2+e2

truelove = str(love) + str(true)

truelove = int(truelove)

if truelove > 10 or truelove > 90:
  print(f"you score is {truelove}% you go together like coke and mentos.")
elif truelove >40 and truelove < 50:
  print(f"your score is {truelove}you are alright together.")
else:
  print(f"your score is{truelove}")


