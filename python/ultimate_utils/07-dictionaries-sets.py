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
#emails[[5, 3]] = "nope" 



######### LOOPING THROUGH KEYS #########
######### LOOPING THROUGH KEY-VALUE PAIRS #########
######### SETS EXPLAINED #########
######### REMOVE DUPLICATES FROM LIST / CREATE SET FROM LIST ##########
######### UNION AND INTERSECTION #########
######### DIFFERENCE AND SYMMETRIC DIFFERENCE ######### 
