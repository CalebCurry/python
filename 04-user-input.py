#Here is a simple exmaple on how to get user input
#we've talk about output with print, but this is just half of input + output

#it's besst practice to tell the user what to do:
print("What is your name?")
name = input()

#Now where does the value they type go?
#the input method actually returns it, so save it to a variable.

#we can then use it like any other variable (because it is just a variabe now)
print("hello " + name)

#althougn this seems silly or simple, this is actually quite revolutionary.
#This is the first point in time where we can make our applications dynamic
#dynamic == changing. The output changes based on the input! WOW!

#input always reads as a string. Example:
print("What is your favorite number?")
num1 = input()

print("what is your second favorite mumber?")
num2 = input()

print(num1 + " + " + num2 + " = " + num1 + num2) # 7 + 5 = 75??? WHAT!?

########## TYPES AND CASTING ##########
#At this point we know there are different types
#but how do we check what type and modify it?

print(type(num1)) #num1 is of type str (string, that is)

#We can cast it to a new type like so:

new_num1 = int(num1)
new_num2 = int(num2)

print(type(new_num1), type(new_num2))

print(num1 + " + " + num2 + " = " + str(new_num1 + new_num2)) #Better

#if you know you're going to be getting a number, it's best to cast it right away.
#Lets try it again, but this time let's showcase another type...float! 
#float allows values after a decimal point, such as 10.5.
print("Give me a 3rd number (with a decimal this time):")
num3 = float(input())

print("all the numbers added:")
print(num3 + new_num1 + new_num2)