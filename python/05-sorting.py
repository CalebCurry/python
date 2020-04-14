########## SORT METHOD ##########


#This is using python built in method and not custom built
#You can easily sort a list:
work_days = ["Monday", "Tuesday", "Thursday", "Friday", "Saturday"]

work_days.sort() 

print(work_days)
#Remember...no return. Modifies list

numbers = [1, 11, 115, 13, 1305, 43]
print(numbers)
#This is not possible because no return. 
# print(numbers.sort())


numbers.sort()
print(numbers)

#What if you want to sort without messing up original? 
#We can copy. 


########## SORTED - COPY A LIST FOR SORT ##########

numbers = [1, 11, 115, 13, 1305, 43]
numbers_sorted = sorted(numbers)

#This returns a NEW list. so original is unaffected!

print(numbers) #original list
print(numbers_sorted)

#This also allows us to assign a sorted listed immediately.

numbers = sorted([1, 11, 115, 13, 1305, 43])
print(numbers)


########## SORT IN REVERSE ##########


#You can easily get a reverse sorted list.
numbers = sorted([1, 11, 115, 13, 1305, 43])
numbers.reverse()

print(numbers)

#However, sorted has an optional/default parameter
#We can pass a value to it

print(sorted(numbers, reverse=True))



########## CASE INSENSITIVE SORT ##########

#When working with strings, 'a' and 'A' are different.

letters = ['a', 'A', 'abc', 'ABC', 'aBc', 'aBC', 'Abc']

print(sorted(letters)) #Capital is considered first
print(sorted(letters, key=str.lower))


########## SORT BY STRING LENGTH ##########


random = ["a", "A", "aa", "AAA", "HELLO", "b", "c", "a"]
print(sorted(random, key=len))
#no () on function! len refers to function. len() invokes function


########## SORT NUMBERS WITH LEXICOGRAPHICAL SORTING ##########


#We can sort numbers similar to strings 1, 11, 111, 2, 22, 222
numbers = [1, 54, 76, 12, 111, 4343, 6, 8888, 3, 222, 1, 0, 222, -1, -122, 5, -30]
print(sorted(numbers, key=str))

#Basically, when we are working with strings, 
#"111" < "12"  because we compare by character left to right
#So we can cast each to a str using the str constructor 


########## COMPARE NUMERICALLY ##########


#Just like we compared using strings in the previous section, we can do it with numbers
#Talse is 0
#True is 1
#expression evaluates to true and maintains that value
#No data is converted to a float in list. Strings are still strings. #bools are bools.


age = 5
stuff = [True, False, 0, -1, "0", "1", "10", age < 30, "20", "2", "5", "9001", "5.5", "6.0", 6]
print(sorted(stuff, key=float))