me = "Caleb"

#escape character example
print("\n")

me = "C\ta\tl\te\tb\n"

print(me)

#can also use single quotes
you = 'Subscriber'

me = "Caleb" #reset to normal

#passing multiple arguments to print
print(me, you)

#double quotes and single quotes work the same way with the exception of working with quotes inside.
#here are some examples:

single_quotes = 'She said "Hi"'
print(single_quotes)

double_quotes = "She said \"Hi\""
print(double_quotes)

single_quotes = 'I\'m learning!'
print(single_quotes)

double_quotes = "I'm learning!"
print(double_quotes)

#notice we have to escape the same quote as the surrounding quote

#Here are the other escape sequences:
#https://docs.python.org/2.0/ref/strings.html

#Notice that if you want to print \ you must put two
print("\\")

#you can also prefix with r which will make a raw string (ignoring escapes except same quote)
print(r'as raw as I\'ve ever seen. \/\/ () \/\/. \t' ) #only \' is escaped



########## CONCATENTATION ##########

#Use a + to concatenate
msg = me + " + " + you
print(msg)

#Can use comma separated values in print. Automatically uses spaces between
print(me, "+", you)

#You can automatically concatenate literals (actual values with quotes as opposed to variables)
#by putting them one after the other. This is ideal if you need to split a large string up 
#onto multiple lines.
print("my " "name "
    "is " "Caleb")

#You can also use multiline string
print("""Name: Caleb
Age: 58""")

#skip newline using \ (without it, it would go down a line each line)
print("""\
Name: Caleb. \
Age: 58""")

"""You may see
them as multi-
line comments even
if they technically
are not. 
https://stackoverflow.com/questions/7696924/is-there-a-way-to-create-multiline-comments-in-python
"""

########## INDEXES ##########

#It's very common to grab particular characters within a string
#this is also common for collections when we get to em.
msg = "This is a very important message."
print(msg[5]) 

#indexing is zero based. This means 0 will get the very first character:
print(msg[0])

#This value is returned and can be assigned to a variable or used in an expression
first_letter = msg[0]
print(first_letter + "acos")

#You can also index from the right.
period = msg[32] #from left
print(period)
period = msg[-1] #from right
print(period)
#This may be obvious, but we do not use -0 to get the first element from the right as we would
#use 0 to get the first element from the left. (Side note) -0 actually is 0:
print(-0) #(side note)
print(0 == -0) #0 == 0 (side note)

########## SLICING #########

#repeating this for ease of reading:
msg = "This is a very important message."

#We can pass two numbers in for the index to get a series of characters.
#left is included. Right is excluded.

#this will get 2 characters (from index 1 - 3 with 3 not included...we are left with index 1 and 2. 
print(msg[1:3]) #hi

#You can also leave off first to start at beginning
#or leave off second to go to end
print(msg[:5]) #print index 0-4 (because 5 is excluded, remember)
print (msg[1:]) #from index 1 to end

#We can also use negatives. Here is how you get the last 8 characters:
print(msg[-8:]) #start 8 from right and go to end

#out of range index
#Grabbing an out of range index directly will cause an error. 
#But incorrect ranges fail gracefully.
#print(msg[42]) #doesn't work
print(msg[42:43]) #works 


########## IMMUTABILITY ##########

#Strings are immutable, meaning they can't change.
cant_change = "Java is my favorite!"

#cant_change[0] = K .....nope. Sorry Kava (my dog)

#generate new string from old:
#Kava is my favorite!
new = 'K' + cant_change[1:]
print(new)

#Python is my favorite!
fav_language = "Python " + cant_change[5:]
print(fav_language)

#Java is actually coffee
coffee = cant_change[:8] + "actually coffee" #grab first 7 characters (index 8 not included)
print(coffee)

#operations that appear to change string actually replace:
#Java is actually coffee (contrary to popular belief).
coffee += " (contrary to popular belief)."
print(coffee)

########## GETTING STRING LENGTH ##########

#There is a function we can use....
#similar to how we invoke print to do something for us (output to console)
#we can invoke len to count for us:

print(len(coffee))

#for those from other languages...
#notice we do not say coffee.len()
#coffee.len() XXXXXX
#nope.

#last index is always len() - 1.
name = "Caleb"
print("index 4:", name[4]) #b
print("len(name)", len(name)) #length is 5


########## MORE STRING WORK ##########

#How to convert a number to a string
length = len(name)

print("Length is " + str(length))

#this works however sometimes you just need one combined string instead of components.
#when we use a comma, we are passing in data as separate arguments. 
#fortunately, print knows how to handle it. Other times, we must pass in one string.
#WARNING --> Commas automatically print a space.
print("length is ", length)

#an example of this is if we need a variable. We cannot use a comma:

#BAD
msg = "length is", len(name)
print(msg) #NOT WHAT WE WANTED!

#GOOD
length = len(name)
msg = "length is " + str(length)
print(msg)

#EVEN BETTER
#We can also nest function calls:
print("length is " + str(len(name)))
#The order in which these are invoked are in to out...
#len(name) is first which returns a number.
#this number is passed to str which converts it to a string
#this string is then concatenated with the string on the left
#this final string is then passed to print

#That's the end of your introduction to strings!