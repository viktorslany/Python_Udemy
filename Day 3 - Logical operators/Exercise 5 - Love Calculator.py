# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

lower_name1 = name1.lower()
lower_name2 = name2.lower()

couple = lower_name2 + lower_name1

t = couple.count('t')
r = couple.count('r')
u = couple.count('u')
e = couple.count('e')

true = str(t+r+u+e)

l = couple.count('l')
o = couple.count('o')
v = couple.count('v')
e_1 = couple.count('e')

love = str(l+o+v+e_1)

final_score = int(true+love)

if final_score < 10 or final_score > 90:
    print(f'Your score is {final_score}, you go together like coke and mentos.')
elif final_score > 40 and final_score < 50:
    print(f'Your score is {final_score}, you are alright together.')
else:
    print(f'Your score is {final_score}.')