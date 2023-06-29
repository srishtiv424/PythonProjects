print("Welcome to the Health Quiz :) ")
ans = input("Are you ready to play ")
if ans.lower() == "yes":
    print("Lets start :) ")
else:
    print("Okk!! GoodByeee")
    quit()
score = 0
ans = input("Do you drink 8 glasses of water everyday ??")
if ans.lower() == "yes":
    score += 1
ans = input("Do you participate in physical activities regularly  ??")
if ans.lower() == "yes":
    score += 1
ans = input("Do you wake up early ??")
if ans.lower() == "yes":
    score += 1
ans = input("Do you go to bed on time ??")
if ans.lower() == "yes":
    score += 1
ans = input("Do you eat fruits and veggies regularly ??")
if ans.lower() == "yes":
    score += 1
ans = input("Do you indulge in junk food and desserts ??")
if ans.lower() == "no":
    score += 1

print(f"Your health score is {score} out of 6. Congratulations !!!")
print(f"Your habits are {score/6 * 100} % healthy")


