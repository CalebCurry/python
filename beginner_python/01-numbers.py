age = 25
print(age)

#this is a comment

age1 = 1
age_2 = 2
#invalid name -> age-3 = 3
#invalid name -> 4age = 4
Age = 6 #not recommended
age_of_user = 7 #recommend underscores for multiple words based on this guide:
#https://www.python.org/dev/peps/pep-0008/#function-and-variable-names

#return = 5 --> Cannot assign to keywords
#https://docs.python.org/3/reference/lexical_analysis.html#keywords

########## OPERATORS ##########
result = 20 / 3 #6.6666....
print(result) 

print("Here is a floor version (crop decimal):", 20 // 3) #6

result = 5**2 #raising a number to a power (5^)
print(result)

#You can use round instead. 
print(round(20/3), 0)

print(result / age) #can use variables in place of literals. This will not change variable values

#guess the output:
print(20 / 3 + 1)

#think of it like this because of operator precedence:
print((20 / 3) + 1)

#You can, however, force certain operations to happen first with ()
print(20 / (3 + 1))

######### MODULUS AND POWER ############

#5 * 5 * 5 * 5* 5
print(5**5)

#The remainder of 78 / 11 is 1.
print(78 % 11)








