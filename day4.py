# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print("we have the following names  ") 
print(names)
import random
x = len(names)
random_position = random.randint(0, x)
print("get set, we are about to roll the dice")
print(" I hope your wallet is heavy")
print(random_position)
print(f"the roulette select {random_position}")
who_pays = (names[random_position])
print(f"{who_pays} is paying for meal")
print("the lucky name is " + who_pays)