######### INTRO TO DICTIONARIES #########

#dictionary stores key-value pairs
#The equiv of an associative array/hash table
emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com" 
}

print(emails)
#in this case, the key is the name, email is the value. 
#Data type doesn't matter at all for the value.
#Key must be a hashable --> What does this mean?
#Classes have a function __hash__ invoked when used as the key
print(hash("hello")) 

#Almost always immutable type
#a tuple will work, list will not. a number will work

#Why use a hashtable? Extremely fast to add or look up data
#O(1) --> constant time. More elements does not mean slower unlike a sort or something
#https://en.wikipedia.org/wiki/Hash_table
#Hashtables often used for memoization

#Next up we gonna talk about retrieving data from a dictionary


######### RETRIEVE DATA FROM DICTIONARY ##########
print(list(emails))
print(sorted(emails))
#print(emails[0]) # NOPE!
print(emails["Caleb"])

#Since data is not nicely sequenced
#we may want to check before we try grabbing stuff

if("Caleb" in emails):
    print("Emailing", emails["Caleb"])

#This may seem bad because we first check to see if its in
#Then we do another line to get the value
#but this is different than a list where we iterate to find the element
#The key is goes through hash to calculate index. Either there or not
#This is O(1)

#You may still not like the casing and in that situation there is a method

print(emails.get("Ryan")) #Returns none if not found
print(emails.get("Ryan", "Not found")) #optional return arg if not found


######### ADD DATA TO DICTIONARY #########


#How to add data (3 ways here):
#indexing
emails["josh"] = "josh@j.com"
print(emails)

#update function
emails.update( {"josh": "evennewer@email.com"})
print(emails)

#Weird variation
emails.update(josh = "new@email.com")
print(emails)

#Key must be hashable
emails[5] = "test"
emails[(1, 2)] = "yep"
#emails[[5, 3]] = "nope" #list is not hashable (mainly cuz mutable)


######### LOOPING THROUGH KEYS #########

#dictionary is an iterable (implements __iter__)

emails = {
    "Caleb":"caleb@email.com", 
    "Gal":"g@example.com",
    "Ted": "talk@gmail.com"
}

#k is a variable but k by convention for key
for k in emails:
    print(k)

#You can use the key to get the element 
#(but will show better way in next section)
for k in emails:
    print("index", k, "is", emails[k])


######### LOOPING THROUGH KEY-VALUE PAIRS #########


#In the prev section we used the index with [].
#Although it works, you can do this:

for k, elem in emails:
    print(k, elem)

#Each iteration k will be the key and elem will be the item found at this key.


######### SETS EXPLAINED #########


#Sets are similar to dictionaries in that the data is hashed and it is unordered.
#Sets are similar to lists in that they just contain the data and not a key-value pair
#Sets are different than lists in that you cannot have duplicates


#we used set with list com STOPPED HERE

######### REMOVE DUPLICATES FROM LIST / CREATE SET FROM LIST ##########
######### UNION AND INTERSECTION #########
######### DIFFERENCE AND SYMMETRIC DIFFERENCE ######### 
