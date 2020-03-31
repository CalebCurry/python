########## NESTED FOR LOOP PT2 ###########


#The previous section had this loop. 
#The only thing we did was print j and a new line.
for i in range(4):
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#Review this and make sure you understand what is going on.

#We could also say what iteration of the outer loop we are on
for i in range(4):
    print("iteration " + str(i), end=": ")
    for j in range(5):
        print(j, end=" ")
    print() #go to next line

#We could also do a more complicated loop to work with the numbers.
for i in range(4):
    print("Count by " + str(i), end=": ")
    for j in range(5):
        print(j*i, end=" ")
    print("...") #go to next line

#What's going on here? 
#We are taking the outer iteration variable and multiplying to by the inner
#in other words, we are counting to 5 each time
#but we are multiplying the result by 0, 1, 2, 3

########## OUTER LOOP VARIABLES IN INNER range() - TRIANGLES #########

#I had no idea what to call this section. Whatever.

#We can always use the outer loop iteration variable within the inner loop.
#What if we wanted to count to 9 for each iteration,
#but start with a higher number each time?

for i in range(10):
    for j in range(i, 10):
        print(j, end=" ")
    print()

#The first iteration i will be 0, so we get: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#The second iteration i will be 1, so we get 1, 2, 3, 4, 5, 6, 7, 8, 9
#etc. 


########## NESTED WHILE ##########


#We now have to worry bout the initialization and increment.

#print 0-4, 4 times:
i = 0
while i < 4:
    j = 0
    while j < 5:
        print(j, end=" ")
        j += 1
    print()
    i += 1

#not as clean...initialization and inrement has to be correct
#pay close attention

#This won't work as expected:

print("Let's try this again:")
i = 0
j = 0
while i < 4:
    while j < 5:
        print(j, end=" ")
        j += 1
    print()
    i += 1

print("What happened?") #j is never reset back to zero


########## LOOP TO SUM ALL NUMBERS ##########


#I want to calculate the sum of numbers 0-10: 10+9+8+7+6+5+4+3+2+1

sum = 0
j = 10
while j > 0:
    sum += j
    j -= 1
print(sum) #55 

#But now I want to get the sum of 9-0, 8-0, 7-0, 6-0, etc...
#Here will be the structure:

i = 10
while (i > -1): #include zero. Could also do >= 0
    #print sum from i to zero. 
    i -= 1


#We just coded how to sum to zero...so copy/paste that there....
#change to j = i (dynamic from 10 to 0)
print("All the sums:")
i = 10
while (i > -1): 
    sum = 0
    j = i
    while j > 0:
        sum += j
        j -= 1
    print(sum) 
    i -= 1

#We can now customize the output to be more readable:
print("All the sums with output:")
i = 10
print("Getting sums up to", i)
while (i > -1): 
    sum = 0
    j = i
    while j > 0:
        if j > 1:
            print(j, "+", end=" ")
        else:
            print(j, "=", end=" ")
        sum += j
        j -= 1
    print(sum) 
    i -= 1