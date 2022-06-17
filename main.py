# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆
import random

final = random.randint(0, len(names) - 1)
#Write your code below this line 👇

print(f"{names[final]} has to pay.")



