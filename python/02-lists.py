########## INSERT INTO MIDDLE OF LIST ##########

#Lists are ordered, and this order may matter to you. 

work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

#OVERTIME!
work_days.insert(2, "Wednesday") #index, "data"

print(work_days)

#What if we want to do the opposite and take a day out?


########## REMOVE ELEMENT FROM LIST BY VALUE OR INDEX ##########


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
"pizza slice", "nunchucks", "pizza slice", "sandwich from mcdonalds"]

backpack.remove("pizza slice")
print(backpack) #SO MUCH PIZZA!

while("pizza slice" in backpack):
    backpack.remove("pizza slice")

print(backpack)

#This may not be the most optimized solution as each removal requires
#an iteration from backpack.count. 
#You should also avoid modifying a list while iterating, so a for-in loop is bad

#for item in backpack:
#    if(item == "pizza slice"):
#        backpack.remove(item)

#The original solution is fine for removing data from reasonably sized lists

#Here is a better solution:
backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

for item in backpack[:]: #uses copy to keep index
    if item == "pizza slice":
        backpack.remove(item)

print(backpack)

#Here is a list comprehension version:
backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchucks", "pizza slice", "pizza slice", "sandwich from mcdonalds"]

backpack[:] = [item for item in backpack if item != "pizza slice"]

print(backpack)

########## REVERSE LIST ##########


backpack = ["pizza slice", "button", "pizza slice", "fishing pole", 
"pizza slice", "nunchicks", "pizza slice", "sandwich from mcdonalds"]

print(backpack)
backpack.reverse()
print(backpack)


########## SWAP AND REVERSE ALGORITHMS ##########

data = ["a", "b", "c", "d", "e", "f", "g", "h"]

for index in range(len(data) // 2):
    data[index], data[-index-1] = data[-index-1], data[index]

print(data)


########## REVERSED ITERATOR ##########


data = ["a", "b", "c", "d", "e", "f", "g", "h"]

data_reversed = []

for item in reversed(data):
    data_reversed.append(item)

print(data)
print(data_reversed)


########## REVERSE USING SLICING ##########

data = ["a", "b", "c", "d", "e", "f", "g", "h"]
data[:] = data[::-1]
print(data)