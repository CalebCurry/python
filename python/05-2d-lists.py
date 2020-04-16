########## WORKING WITH 2D LISTS ##########

grades = [[6, 3, 5], [60, 43, 4, 23], [205]]

#This may be review
#First list in grades:
print(grades[0])
print(type(grades[0])) #list

#Second element of first list in grades:
print(grades[0][1])
print(type(grades[0][1])) #int

#Lists are dynamic
grades.append([4]) #add an element, increasing len
grades.pop(1) #indexes rearranged
print(grades)
#grades.clear() #remove all.
print(len(grades))
print(len(grades[0]))
#Python keeps it simple in that there's not a static array type.
#Other languages often have an array and then list. 

#iterate through 2D list
for inner_list in grades:
    for grade in inner_list:
        print(grade, end=" ")
    print()

#This will break if one element is not in a list. You COULD check, if you want.

#checking if list:
grades = [[6, 3, 5], [60, 43, 4, 23], 5, 3, [205]]

for inner in grades:
    if  isinstance(inner, list):
        for grade in inner:
            print(grade, end=" ")
        print()
    else:
        print(inner)
    
#You can also iterate using range

grades = [[1, 2, 3], [4, 5, 6, 7, 8], [9]]

for i in range(len(grades)):
    for j in range(len(grades[i])):
        print(grades[i][j], end=" ")
    print()

######### FUNCTION TO PRINT LIST ##########

def print_2d(passed_in):
    for inner in passed_in:
        if isinstance(inner, list):
            for data in inner:
                print(data, end=" ")
            print()
        else:
            print(inner)
    
print_2d(["chickity", "china", "chinese", "chicken", [1, 3, 3], [4]])


########## JOIN ##########


data = ["01001100", "01001111", "01001100"]

print(".".join(data))
print("-".join(data))

data = [1, 0, 1, "2", "505"]
print(" ".join(str(x) for x in data))
#100% original idea stolen from this guy
#https://stackoverflow.com/questions/3590165/join-a-list-of-items-with-different-types-as-string-in-python


########## SORTING 2D LIST ##########

data = [[10, 2, 3],[10, 20], [4, 5000, 6], [7, 8, 9], [10]]

print(sorted(data))

#behind the scenes a comparison is done. Here's some more practice
print([10] < [11]) #True
print([1, 10] < [1, 2]) #False

#What about this?
print([5] < [5, -1]) #True
#the shorter is considered less


########## Sorting by sum of list #########


#We can also sort using a different function to determine which comes first:

print(sorted(data, key=sum))

#You can also reverse the order:
print(sorted(data, key=sum, reverse=True)) #each list stays same, just order of list is flipped


########## CUSTOM KEY FUNCTION ##########


#Any fuction you could use on a list to manipulate the data should do the trick
#Here's another example:

def avg(data):
    avg = sum(data) / len(data)
    print(data, "average is", avg) #for our sake to see
    return avg

data = [[5, 5, 5], [3, 4, 5], [3, -3, 0], [1,1,1,79], [1, 10, 1, 20]]
print(sorted(data, key=avg))