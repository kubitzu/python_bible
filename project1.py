import random

health = 50
difficulty = 1
new_difficulty = random.randrange(1, 4, 1)

potion = random.randrange(25, 50)

print("Health: ", health)
print("Difficulty: ", new_difficulty)
print("Potion: ", potion)

print(int((health + potion)/new_difficulty))



