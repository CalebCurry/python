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

########## RETURN #########

#Return works in a similar way except that it will only skip the rest of the iteration.
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