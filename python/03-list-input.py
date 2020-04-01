########## SPLIT ##########

msg = "Pay attention to each word that I say..."
words = msg.split() #returns list
print(words)

msg = "this,is,important,data" #How to parse CSV
print(msg.split(","))


########## SPLIT STRING BY LINE ##########


#This may have came from a file, for example.
msg = """\
Hey there.
My name is Caleb!
What's your name?
You're name is NERD? Weird...
Bye for now!"""

print(msg) #to see how it is stored...

print(msg.split('\n'))

########## INPUT USING SPLIT ##########

print("List your favorite foods separated by ', '")
print("Example input: ")
print("Kale, bok choy, brussel sprouts")

foods = input().split(', ')

for food in foods:
    print("You said " + food)

#an obvious downfall is that this is very touchy.
#instead, we could ask one food per line

########## LOOPING TO GET USER INPUT ##########

fav_foods = []
while True:
    print("Enter a food. q to quit: ", end="")
    fav = input()
    if str.lower(fav) == 'q':
        break
    fav_foods.append(fav)

print("all foods:", fav_foods)


########## LIST AS STACK ##########

#Consider a stack of plates. 
#The last one you add is the first to be removed.

#The data structure depends on adding to the end of a list:
stack = []
stack.append("added")
#and removing from the end of the list
stack.pop() 

fav_foods = []
while True:
    print("Enter a food. q to quit, r to remove: ", end="")
    fav = input()
    if str.lower(fav) == 'q':
        break
    if str.lower(fav) == 'r':
        popped = fav_foods.pop()
        print("removed " + popped)
        print("all foods:", fav_foods)
        continue
    fav_foods.append(fav)
    print("all foods:", fav_foods)

print("final foods:", fav_foods)


########## QUEUE VARIATION ##########


#The difference with a queue is that the first added is the first removed
#consider a line to a roller coaster
#first in line rides ride first.

#The data structure depends on adding to the end of a list:
stack = []
stack.append("added")
#and removing from the FRONT of the list
stack.pop(0) #remove index 0

fav_foods = []
while True:
    print("(QUEUE) Enter a food. q to quit, eat to remove: ", end="")
    fav = input()
    if str.lower(fav) == 'q':
        break
    if str.lower(fav) == 'eat':
        popped = fav_foods.pop(0)
        print("removed " + popped)
        print("all foods:", fav_foods)
        continue
    fav_foods.append(fav)
    print("all foods:", fav_foods)

print("final foods:", fav_foods)