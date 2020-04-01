#Welcome. We are going to be working through python
#It should be pretty easy to follow along with but if you struggle
#I have a beginner series as well


########## APPEND TO LIST #########


healthy = ["pizza", "frozen custard"]

healthy.append("apple crisp")

print(healthy)


########## CHECKING IF ELEMENT IN LIST #########


#Obviously on our health adventures we want to know if something is healthy.

print("chicken pot pie" in healthy)

#This returns True / False. Can use in keyword within if

backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in healthy):
    print("eating it")

#We can make this more dynamic. Let's remove chicen pot pie from list. 


########## REMOVING FROM LIST ##########


healthy = ["pizza", "frozen custard"]
backpack = ["pizza", "chicken pot pie", "kale chips"]

if("pizza" in healthy):
    backpack.remove("pizza")

print(backpack)


########## COUNTING ELEMENTS IN LIST ##########

healthy = ["pizza", "frozen custard"]
backpack = ["pizza", "chicken pot pie", "kale chips"]

print(len(healthy), len(backpack))

#You may think of something like healthy.size() or healthy.length() or even healthy.count()
#This is not quite what we are looking for. 
#count is used to count a particular element in a list. Up next!


########## COUNT / CHECK IF ELEMENT EXISTS ##########


print(backpack.count("pizza")) #number of pizza in list

backpack = ["pizza slice", "pizza slice", "pizza slice"]

print(backpack.count("pizza slice")) #3

#This can be used to prevent too many items:

if(backpack.count("pizza slice") < 3):
    backpack.append("pizza slice")
    print("You put a piece of pizza in your backpack")
else:
    print("How about you go to the gym?")


########## INSERT INTO MIDDLE OF LIST ##########


#Lists are ordered, and this order may matter to you. 

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

#OVERTIME!
work_days.insert(3, "Wednesday") #index, "data"

print(work_days)

#What if we want to do the opposite and take a day out?


########## REMOVE ELEMENT FROM LIST BY INDEX ##########


#We learned how to remove by value:

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

#VACATION DAY!
work_days.remove("Saturday")
print(work_days)

#However, removing by index is also useful:
work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

del work_days[0]
print(work_days)


########## REMOVE ELEMENT WITH POP ##########


#The benefit here is the method returns the element
work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]
popped = work_days.pop(1)

print("You removed " + popped)
print(work_days)


########## REMOVE ELEMENT FROM LIST USING DEL AND SLICE ##########


work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

del work_days[0:2] #remove first 2
print(work_days)

del work_days[-2:] #remove last 2 (start 2 from right and go to end)
print(work_days)


########## REMOVING ALL OCCURANCES IN LIST ##########

backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchicks", "pizza slice", "sandwich from mcdonalds"]

backpack.remove("pizza slice")
print(backpack) #SO MUCH PIZZA!

while(backpack.count("pizza slice") > 0):
    backpack.remove("pizza slice")

print(backpack)

#This may not be the most optimized solution as each removal requires
#an iteration from backpack.count. But it's cleanest
#You should also avoid modifying a list while iterating, so a for-in loop is bad

#for item in backpack:
#    if(item == "pizza slice"):
#        backpack.remove(item)

#The original solution is fine for removing data from reasonably sized lists
#for very very large lists, look into list comprehension 
#Which we are not getting into quite yet. 


