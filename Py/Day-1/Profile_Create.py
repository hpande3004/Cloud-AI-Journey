# PROFILE CREATION SAMPLE PROGRAM

name = input("Enter your name: ")
age = input("Enter your age: ")
experience = input("Enter your experience: ")
cloud = input("Enter your preferred cloud: ")

print("\n-------Profile-------")
print("Name: " ,name)
print("Age: " ,age)
print("Experience: " ,experience)

if int(experience) < 5:
        print("You are a junior")
else:
        print("You are a senior")
print("Preferred Cloud: " ,cloud)

if cloud=="AWS":
        print("You are Amazon engineer")
else:
        print("You are cloud engineer")