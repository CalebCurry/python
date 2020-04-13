########## BREAK ##########
#You can break out of a loop any time using the break keyword.
#For example, if you are looking for a particular elemennt 
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "Python":
        print(language + " found")
        break

#Things after break within same block never get hit
#Things outside of the if can still be hit if break is not hit first

for language in languages:
    if language == "C++":
        print(language + " found")
        break
        print("YOU CAN'T SEE ME!")
    print("It's JOHN CENA!!!!") #executes first iteration but not 2nd

########## CONTINUE #########

#continue works in a similar way except that it will only skip the rest of the iteration.
#This may be useful if you need to continue iterating through the list
#(in this context you could be looking for duplicates or other interesting lanugages)

print("Searching for Java:")
for language in languages:
    if language == "Java":
        print(language + " found")
        continue
    print(language + ": Not What we are looking for...")


########## ELSE INSTEAD OF CONTINUE

#This same structure can be achieved with an else

print("Searching for Perl:")
for language in languages:
    if language == "Perl":
        print(language + " found")
    else:
        print(language + ": Not What we are looking for...")


########## HOW TO DO NOTHING ##########


for x in range(10):
    pass

#You can do this when...uh... hmm.....why WOULD you want to do this?
#My bet is that this is the equivalent to TODO. AKA come back to it later to finish.
#This can also be used for a busy wait... Keeping processor busy.


######### ELSE WITH FOR ##########

#This one is actually new to me. You can use an else with a for.
#This will execute anytime the for loop hits the end of iterable (range or list)

for i in range(0,10):
    print(i, end=" ")
else:
    print("done")

#This can be useful for a failed search as an example because it will not be hit with break
for language in languages:
    if language == "Alabama":
        print(language + " found")
        break
else:
    print("Nope.")


######### While loop ##########


#Another form of loop is the while loop.
#Here is an example that counts 0-9 (including 0 and 9)

i = 0 #initialize
while(i < 10): #condition
    print(i, end=" ") 
    i += 1 #update
print()


#customize the loop as you please! Here's how to count down by two
i = 30 
while(i >= 0):
    print(i, end=" ") 
    i -= 2 
print()


########## CONVERTING WHILE TO FOR AND BACK ###########


#I think it is important to comfortably work with for and while
#Both loops need an initialization, condition, and update.

initialization = 5
stop_at = 10
increment = 1

for i in range(initialization, stop_at, increment):
    print("for loop:", i)


while(initialization < stop_at):
    print("while loop:", initialization)
    initialization += increment


#To make them match, the update should come at the end of the while
#When passing a variable to range, the variable is not affected
#Range returns new data and initialization is left at 5. 


########## ELSE WITH WHILE ##########
#The else statement for a while will execute if no break is hit. 

i = 0 
while(i < 10): 
    print(i, end=" ") 
    i += 1 
else:
    print("Else of while")

#Random other example
#Checks to see first square > 

i = 0 
while(i < 10): 
    if i**2 > 50:
        print("First square big enough:", i)
        break
    i += 1
else:
    print("None are big enough")


########## FLAG VARIABLES ########## 


#You may not be comfortable with else after a loop
#The equivalent without an else would be like so:
index = -1 #keeps -1 until told otherwise
i = 0 
while(i < 10): 
    if i**2 > 500:
        index = i #change index if requirements are met. Not reached because > returns false
        break
    i += 1

if index > -1:
    print("First square big enough:", i)
else:
    print("None are big enough") 

#Setting a starting value (such as -1), possibly changing it, 
#and checking it afterwards creates a flag variable.
#Just a concept. Nothing new on syntax

######### "DO WHILE" loop ##########

#In other languages, there is a concept as a do-while loop. 
#These loops always execute at least once.
#We can mimmick this in python easily.

i = 15
print(i) #prints i atleast once no matter what
i += 1
while (i < 10):
    print(i)
    i += 1


#To generalize this:

#do stuff
#condition - true to continue
    #do stuff 

#This structure is useful for sentinel / indefinate loops


########## Indefinate / Sentinel loops ##########

#an Indefinate loop is a loop that we do not decide how long it will run ahead of time
#The loop can be stopped, however. This makes it different than an infinate loop.
#An example may be displaying a menu numerous times


print("Do you want to continue? Y/N: ") 
response = input()
while response == "Y" or response == "y":
    print("Do you want to continue? Y/N: ") 
    response = input()  
#a logical name for the variable would be 'continue' or 'in'  
#however these are keyword. don't try it.

#not super common vocab but good to know...
#A sentinel value is a value used to stop a loop. In this case it is anything besides "Y" or "y"
#for programs a sentinel value is often 'q' 


########## UPPER AND LOWER ##########


#We can also write our code like so
print("Do you want to continue AGAIN? Y/N: ") 
response = input()
while response.lower() == "y":
    print("Do you want to continue? Y/N: ") 
    response = input()  

#This is important to understand as "Y" and "y" are not the same thing
#Overlooking this can introduce logical bugs in our software

#There is also an upper.
#We can also invoke it on constant strings
print("am i screaming?".upper())

########## checking if a string is uppercase or lowercase ##########

name = "Caleb"
if name.isupper():
    print("Upper")
elif name.islower():
    print("Lower")
else:
    print("Mixed")

#not sure when you might need this but still good to know.