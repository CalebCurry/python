#What is a list?
#It's a type of collection. just like what it sounds...It holds numerous things.

ages = [20, 25, 20]

#Here is a list of strings
names = ["Caleb", "Emily", "Sabrina"]

#We can even mix types of data:
my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]
#Here we have a list of a string, number, and another list. 
#We will get into nested lists soon.

#We can print an entire list by using the list name
print(ages)
print(names)
print(my_favorite_things)

######### INDEXING ##########

#Similar to strings, we can use indexes to grab particular elements
print(ages[2]) #grab 3rd element.
#remember, these are zero based! The first element is index 0.

#Indexing can also return a list (doesn't modify original list)
print(my_favorite_things[2]) 

########## UPDATING AND SLICING ##########
#lists are different than strings in that the data can be changed!
#how to update a list element
ages[0] = 5
ages[1] = 10
ages[2] = 15
print(ages) #Updated!

#What about slicing?
print(ages[1:]) #It works!
#Now all the skills you learned with strings seem more valuable, huh?

#Since lists are mutable, can we combine slicing with updating data?

ages[1:] = [6, 7]
print(ages) #MY GOODNESS it worked. 
#Confused on what we did? We sliced to get all of the data index 1 and beyond...
#but instead of printing it, we assigned it a new list of 6 and 7. 


########## COPYING LISTS ##########

#You may think copying lists is easy:
names = ["Caleb", "Emily", "Sabrina"]
names2 = names #copied? NOOO

#The problem here is that they both point to the same list in memory.
#Changes in one are visible in the other 
names2[0] = "Kaylub" #Change to names2
print(names) #printing name1 and seeing "Kaylub"

#This is great if we want an ALIAS! But not if we want a COPY!
#Here is how to copy:
names = ["Caleb", "Emily", "Sabrina"]
names2 = names[:]
#remember slicing doesn't modify the original list. 
#leaving no number on the left of : says "All the way from beginning"
#leaving no number on right of : says "All the way to end"
#in other words...[:] returns the whole list. 
names2[0] = "Kaylubbbbb"
print(names) #Caleb YAAYYYYY

#another Option is to use a method on the list...copy()
names1 = ["Caleb", "Emily", "Sabrina"]
names2 = names1.copy()
names2[0] = "Kaylubbbbb"
print(names) #Caleb YAAYYYYY

#Notice that we say list.copy() instead of copy(list). 
#This is called a method instead of a function because it's attached to an object
#We'll get into methods later.
#This is also a shallow copy. Will discuss the difference in a bit.

########## NESTED LIST BASICS ##########

#Earlier we created this list
my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]

#The third element is actually a list itself.
#Although we are going to get into nested lists in more detail later on, I wanted to give basics
#Becuase the 3rd element is a list, you can get that list like so:

streaming = my_favorite_things[2]
print(streaming)

#You can treat it like a normal list (because it is)
print(streaming[1])

#This works, however a more useful way of grabbing an element from a nested list is like so:
print(my_favorite_things[2][1])
##first [] is outer list. second [] is inner list. 

#This can be repeated even deeper.
nested_list = [[[[["deep dive"]]]]]
print(nested_list[0][0][0][0][0]) #Got it!

#Because of the versatility of lists, you'll see them a lot. 


########## SHALLOW COPY EXPLAINED ##########


#Copying a list as so makes a shallow copy. 
#This means that any complex types will not be copied but rather available in both
#The easiest way to understand this is with an example. 

my_favorite_things = ["Working out", 7, ["netflix", "Amazon Prime"]]
my_favorite_things2 = my_favorite_things.copy();

#modify the original
my_favorite_things[2][0] = "Audible"
print(my_favorite_things2) #CONTAINS AUDIBLE 
#this is because the reference to nested list is copied, not the entire list itself.
#(the copy points to the same data)


########## DEEP COPY ##########


#The alternative to a shallow copy is a deep copy. 
#In order for us to do a deep copy, we must have an import
import copy
#copy is an example of a module. you'll often find all the imports at the top.
#but it's my project so yolo.

#Now we can use copy.deepcopy method
#This method returns a new list so we can assign it to a variable.
my_favorite_things3 = copy.deepcopy(my_favorite_things)
#now we modify the original
my_favorite_things[2][0] = "Hulu"
print(my_favorite_things) #contains Hulu
print(my_favorite_things3) #No Hulu to be found. keeps Audible value.

########## CoOMBINING LISTS #########

#similar to how we can concatenate strings, we can combine lists
msg = "he" "llo" #again, + is optional with string literals
print(msg)

good = ["kale", "brocoli", "spinach"]
bad = ["pizza", "fries", "wings"]

just_right = good + bad
print(just_right)

#This may be obvious by now, but any time we assign an expression to a variable,
#we can skip the variable altogether and use the expression

print(good + bad)

