
name = input ("Welcome to a mini quiz game! What is your name?: ")
score = 0
answer1 = input("""What is the capital of France?
a) Paris
b) London
c) Rome
Your answer:""")

if answer1.lower() == "a" or answer1.lower == "paris":
    score =score + 1
    print(f"Congratulations {name}!!! You scored it right")
else:
    print("Wrong answer the correct answer is a:Paris")



answer2 = input("""2)What is 3 + 2?
a) 2
b) 4
c) 5
Your answer:""")

if answer2.lower() == "c" or answer2.lower == "5":
    score =score + 1
    print(f"Congratulations {name}!!! You scored it right")
else:
    print("Wrong answer the correct answer is c:5")



answer3 = input("""3)What is 6 + 2?
a) 2
b) 8
c) 5
Your answer:""")

if answer3.lower() == "b" or answer3.lower == "8":
    score =score + 1
    print(f"Congratulations {name}!!! You scored it right")
else:
    print("Wrong answer the correct answer is b:8")

percentagescore = int((score/3) * 100)

print(f"Thankyou {name} for participating in this quiz\n"
f"You scored {percentagescore}%")

