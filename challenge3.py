
import random
names = ["Cowboy", "Mechanic" "Bwoh" "From the scratch" 
"Wordpress" "Front-end" "Back-end" "Fullstack", "Pure brain work", "Php", "Python"
"Javascript", "Dart"]

index = random.randint(0,12)
dev_type = names[index]

while True:
    def cowboy():
        username = input("Enter your name to get started: ").lower()
        print(username,"you're a ",dev_type," dev")

print("Hey, I think it's time you know your future as a developer")
cowboy()
print("Play again if you don't believe me")
while True:
    prompt = input("Do you want to play again? ").lower().strip
    if "yes" in prompt:
        cowboy()
    elif "no":
        break
print("B E L I E V E")
