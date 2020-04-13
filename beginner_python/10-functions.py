#We are going to wrap back around to lists and loops
#but first functions
#functions are the only way to build scalable code


########## HOW TO CREATE A FUNCTION ##########


#This one is simple, but we go on.
def greet():
    print("hello")
    print("Welcome, Caleb")

#invoke
greet()
#Can invoke numerous times:
greet()
greet()

#Benefits: We can save lines of code if function is large
#One source of truth. No repeat of code. Need changes?
#update one spot
#Can improve code readability


########## Arguments and Parameters ##########


#parameter is a variable used within a function 
def greet(name): #name is a parameter
    print("hello")
    print("Welcome, " + name)

greet("Sabrina") #Sabrina is an argument (value passed in to parameter variable)

#We can also use variables as arguments

new_guy = "Carl"
greet(new_guy)

#This gives the value "Carl" to the name parameter


########## RETURN  ##########


#We can return (exit) from a function in certain situations
def greet(name):
    if name == "Claire":
        return
    else:
        print("hello")
        print("Welcome " + name)

greet("Claire") #NOPE!
greet("Clarice") #YES!

#This code can be simplified by removing the else:

def greet(name): 
    if name == "Claire":
        return
    print("hello")
    print("Welcome " + name)

#The concern without an else is that the line after the if is announced regardless of name
#This works, however, because there is never a case where name == "Claire" that is not returned
#We only need else if we are not returning!


########## RETURN VALUES ##########


#instead of printing inside the function, we can use the function to generate a message
#We can print outside of the function on the caller side 
#caller side --> Where we invoke the function

def greet(name): 
    if name == "Claire":
        return "Go away"
    return "Hello " + name + "! Welcome to my app."

returned = greet("Sal")
print(returned)

#We can use the returned value directly...
print(greet("Claire"))


########## DEFAULT ARGUMENTS ##########


#We may want to create a method that does not require an input
def greet(name="User"): 
    if name == "Claire":
        return "Go away"
    return "Hello " + name + "! Welcome to my app."

print(greet()) #No name? Default to User


########## MULTIPLE ARGUMENTS / PARAMETERS ##########


def greet(name="User", be_nice=False): 
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

print(greet("Caleb", True))
print(greet("Caleb"))


########## KEYWORD ARGUMENTS ###########

#This will showcase how to skip any particular parameter

def greet(name="User", be_nice=False):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

print(greet(be_nice=True)) 

#NOTE if a parameter does not have a default value, you must specify it
#Either in order without a name, or assigning by name


########## POSITIONAL OR KEYWORD ARGUMENTS ##########


#With the function we have defined, we can pass arguments by position or by keyword

def greet(name, be_nice):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name


print(greet("Positional", True))   #Positional
print(greet(be_nice=True, name="Keyword")) #Keyword (NOTICE ORDER!)

#Positional arguments must follow keyword arguments
#ERROR: 
#print(greet(be_nice=True, "Keyword"))

#NOTE that we can invoke by position or keyword. We can restrict to either though.
#If we want our method to have to be invoked using position, we can do that
#We can also restrict to keyword only as well.


########## POSITIONAL-ONLY ARGUMENTS ##########


def greet(name, be_nice, /):  #Anything before the / must be positional
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name


print(greet("positional", False))
#ERROR because invoking with keyword:
#print(greet("Positional", be_nice=True))  

#We can also put the / between arguments
def greet(name, /, be_nice):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

print(greet("Positional", be_nice=True)) #This works now. 
print(greet("Positional", True)) #This works too. 

#We can invoke with be_nice being named or positional
#Doesn't add a lot of value but nice when we have lots of arguments

#ERROR because invoking name by keyword:
#print(greet(name="Keyword", be_nice=True)) 


########## KEYWORD-ONLY ARGUMENTS ##########

#Place a *, before any arguments that are keyword-only
def greet(name, /, *, be_nice ):  #be_nice is keyword only
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

print(greet("Positional", be_nice=True)) #be_nice= is required

#ERROR because positional
#print(greet("Positional", True))


########## SPECIAL PARAMETER SUMMARY ##########

#We've learned about positional-only arguments, and keyword-only arguments
#And of course the arguments that can be either. 
#Here is full (but contrived) example

def do_nothing(pos1, pos2, pos3, /, either1, either2, *, keyword1, keyword2, keyword3):
    print("pos1", pos1)
    print("pos2", pos2)
    print("pos3", pos3)
    print("either1", either1)
    print("either2", either2)
    print("keyword1", keyword1)
    print("keyword2", keyword2)
    print("keyword3", keyword3)

do_nothing(1, 2, 3, 4, either2=5, keyword3=6, keyword1=7, keyword2=8)

#A very helpful rule to remember the positioning of this junk
#You must always invoke a method passing positional first
#Because if you passed them later, the position would be janked up
#The either parameters must be in the middle because they can also be positional
#The keyword are always last because you can mix their order


########## LIST PARAMETERS / FUNCTION TO ITERATE LIST #########


def greet_all(people):
    for person in people:
        print("Hello " + person)

people = ["Caleb", "Josh", "Austin"]

greet_all(people)


########## UNLIMITTED ARGUMENTS / PACKING ##########


#What if you are working with individual pieces of data?
#We can modify the function to "pack" the data with *

def greet_all(*people):
    for person in people:
        print("Hello " + person)


greet_all("Caleb", "Josh", "Austin")


########## UNPACKING ##########


def print_info(name, age, email):
    print(name + " is " + str(age) + ". Reached at " + email)

info = ["Caleb", 12, "email@email.com"]
print_info(*info)


########## FUNCTIONS CALLING FUNCTIONS ##########

#Let's say we have this method and no way to edit it
def greet(name, be_nice=True):  
    if be_nice:
        return "Hello " + name + "! Welcome to my app."
    return "Go away " + name

#We can utilize it.
def greet_all(people):
    for person in people:
        print(greet(person)) #because it returns string

people_to_greet = ["Johnny", "Jimmy", "Jacob"]
greet_all(people_to_greet)