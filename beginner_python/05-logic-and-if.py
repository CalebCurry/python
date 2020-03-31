#Any complex program is made possible thanks to control flow statements
#control flow statements include if statements and loops

########## LOGIC ##########

#You must first understand booleans. 
#They are either True or False (these are both keywords)
#
happy = True
print(happy)

#There are operators that will return true or false
#These are known as comparison operators

print(5 > 3)
age = 21
print("age >= 21?", age >= 21)

#You can also compare strings:
me = "Caleb"
you = "Nerd"
print("me == you?", me == you)

#Even lists!
my_grades = [100, 100, 100]
your_grades = [100, 100, 1]
print("Same grade?", my_grades == your_grades) #false

your_grades = [100, 100, 100]
print("Same grade?", my_grades == your_grades) #true 

#in some languages, == compares by memory address to see if same object
#this is done in python using is.
#This is known as an identity comparison
print("are grades the same object?", my_grades is your_grades) #false

my_grades = your_grades
print("are grades the same object?", my_grades is your_grades) #true

#You can also do order testing for strings
#Read ABC comes before BCD?
print("A before B?", "ABC" < "BCD")

#Not operator can be used to negate an equality check
#Read A is not equal to B? 
print("A != B?", "A" != "B")


########### IF STATEMENT ##########


#You may be wondering the user of all of these conditions. They are used within ifs and loops.
#First, the if statement.
print("What's your name?")
name = input()
print("what's your age?")
age = int(input())

if name == "Caleb":
    print("Hey, Caleb")
#otherwise do nothing and continue
#4 spaces over for indent
#THIS INDENT IS IMPORTANT!

#BAD:
if age > 100:
    print("WOW!")
print("You are so old") #executes EVERY time

#GOOD:
if age > 100:
    print("WOW!")
    print("You are so old")

#It is recommended to use 4 spaces instead of a tab.

########## if elif else ##########

if age > 100:
    print("You're old")
elif age > 120:
    print("How are you even alive?")
else:
    print("You may have some years left in you")


########## CONDITIONS WITH BOOLEANS ##########


#When working with a boolean variable, you may think to do this
caleb_is_cool = False
if caleb_is_cool == True:
    print("Let's be friends")
else:
    print("Eww")


#since the == operator returns True or False, and the variable is already false...
#We can do this instead:
caleb_is_cool = False
if caleb_is_cool:
    print("Let's be friends")
else:
    print("Eww")


########## LOGICAL OPERTATORS #########


#Logical operators can be used to make complex expressions that ultimately evaluate to true or false.
#and --> both must be true
#or --> one must be true
#not --> negates (flips)


#An example with or
thunder = False
lighting  = True

if lighting or thunder:
    print("Don't go swimming!")

#An example with and
car_nice = True
on_sale = False

if car_nice and on_sale:
    print("Buy the car!") #This will not execute!

#An example with not AND and
temp_outside = 50
pool_heated = False

if temp_outside < 60 and not pool_heated:
    print("Don't go swimming!")

#this can be confusing, so it might be best to read it as english
#however, logically... pool_heated is false so not pool_heated is true.
#therefore, both sides are true. 

