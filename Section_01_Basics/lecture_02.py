#This Program asks for your name and asks your age

print("What is your name:") # ask for their name
name = input()
print("Nice to meet you " + name)
print("The lenght of your name is:")
print(len(name))
print("What is your age?") # asks for their age
age = input()
print("You will be " + str(int(age) + 1) +" in a year")