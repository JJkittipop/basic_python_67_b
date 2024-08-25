"""
#
# part: python Function
#
"""
def myFunction():
    i = 1
    while i <= 5:
        print("Hello World " , i)
        i+=1
myFunction()
myFunction()

# parameter
def myName(name):
    print("My name is " , name)
myName("Anya")
myName("Loid")

def myFullName(first_name = "Unknow", last_name = "Forger"):
    print("My name is " + first_name + " " + last_name)
myFullName("Anya")
myFullName("Anya", "Forger")
myFullName("Yor", "Forger")
myFullName(last_name = "Forger", first_name ="Loid")

def myFruit(fruits):
    for fruit in fruits:
        print(fruit)
fruits = ["apple", "banana", "coconut"]
myFruit(fruits)

def redPotion(hp):
    return hp + 50
print("Hp: ", redPotion(100))
print("Hp: ", redPotion(30))
