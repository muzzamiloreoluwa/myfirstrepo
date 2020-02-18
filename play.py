
import random
names = []
print("Welcome to Random Winner!!!")
print("Hey, would you like to play the random winner game? ")
yn = input("Yes or No: ").lower()
if yn == "yes":
    user_in = input("enter a new name: ")
    names.append(user_in)
    x = 1
    while x <= 7:
        input("enter a new name: ")
        names.append(user_in)
        x = x + 1
        if x > 7:
            break
    index = random.randint(0,7)
    random_winner = names[index]
    print("The random winner is " + random_winner)
    print("Thanks for playing. Soon we'll add a while loop nested in def to enable replaying from here, but for now re-run the code to play again.")
elif yn == "no":
    print("Thanks for your time, I can see you're busy.")
