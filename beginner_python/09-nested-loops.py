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


