print("Welocme to my Computer Quiz play!")
 
playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play)")
score = 0

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does USB stands for? ")
if answer.lower() == "universal serial bus":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPS stands for? ")
if answer.lower() == "global positioning system":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does VIP stands for? ")
if answer.lower() == "very important person":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

answer = input("What does HTML stands for? ")
if answer.lower() == "hypertext markup language":
    print('Correct!')
    score += 1
else:
    print('Incorrect!')


print("You got " + str(score) + "question Correct!")
print("You got " + str((score / 6) * 100) + "%.")    
