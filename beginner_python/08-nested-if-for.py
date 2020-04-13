#The only form of nesting we've encountered so far was an if statement within a loop.
languages = ["Python", "C++", "Java", "Perl", "C#"]

for language in languages:
    if language == "C#":
        print(language + " found")
        break

#proper nesting is vital inside of python. Unlike many other languages,
#python is indentation sensitive. The position of the code is important

for language in languages:
    if language == "C#":
        print(language + " found")
    break

#^^ This loop does something completely different.
#Syntactically, the only difference is the position of the break keyword. 
#It will break at the end of the first iteration no matter what

########## NESTED IF ##########

logging = True
logging_in = True
name = "Caleb"

if logging_in:
    if logging:
        print(name + " is logging in.") #log console, file, or db.
    print("Welcome, " + name)

########## CONVERTING COMPLEX CONDITIONAL TO NESTED IF ###########

#It is common in more complex code to see nested if statements
#This can often replace complex expressions that use numerous logical operators
#Either way is not better, just whatever is clearer to you 

age = 20
fun = False
likes_to_dance = True

if (age < 30 or fun) and likes_to_dance:
    print("You're invited to the party!")
else:
    print("get lost freakbag") #most general

#This could alternatively be represented with nested if statements 
#and can allow more specific responses

if age < 30 or fun:
    if likes_to_dance:
        print("You're invited to the party!")
    else:
        print("How could you not like to dance?") #Specific to dancing
else:
    print("You're either too old or not fun enough to be in my party")
    #Note how we can't easily say which. We say OR.


########## INTRO TO NESTED FOR ##########

#If you are fairly new, nested loops can be confusing. Pay attention!
#Stop texting and looking at memes...CODE!
#We can loop a loop using a nested loop.
#The inner loop will run each iteration of the outer loop.

for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#The result? The inner loop prints 0 - 4. We then do this 4 times
#After each complete 0-4 print, we go to the next line with print()
#This puts the next loop on the next line of output