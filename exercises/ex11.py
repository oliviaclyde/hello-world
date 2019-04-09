print("How old are you?", end=' ')
age = int(input())
print("How tall are you?", end=' ')
height = (input())
print("How much do you weigh?", end=' ')
weight = int(input())

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

#Practicing formatting of a string
weather = "It is {} today."
print(weather.format("rainy"))
