def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

printme("Hello world!")

print('-'*60)
############################################################
#Pass by Reference

def changeme( mylist ):
   print ("Values inside the function before change: ", mylist)
   
   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

print('-'*60)
############################################################
#argument is being passed by reference
#and the reference is being overwritten inside the called function.
def changeme2( mylist ):
   mylist = [1,2,3,4] 
   print ("Values inside the function: ", mylist)
   return

mylist = [10,20,30]
changeme2( mylist )
print ("Values outside the function: ", mylist)

print('-'*60)
############################################################
#Keyword Arguments

def printinfo( name, age ):
   #name,age are Required Arguments
   print ("Name: ", name)
   print ("Age ", age)
   return

printinfo( age = 20, name = "ALi" )

print('-'*60)
############################################################
#Default Arguments

def printinfo2( name, age = 35 ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return


printinfo2( age = 25, name = "Ahmed" )
printinfo2( name = "Ahmed" )
printinfo2( "Ahmed" )

print('-'*60)
############################################################
#Variable-length Arguments

def printinfo3( arg1, *vartuple ):
   print ("Output is: ")
   print (arg1)
   
   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
printinfo3( 10 )
printinfo3( 70, 60, 50 )

print('-'*60)
############################################################
# Anonymous Functions

sum = lambda arg1, arg2: arg1 + arg2

print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))

print('-'*60)
############################################################
#return Statement
def sum2( arg1, arg2 ):
   total = arg1 + arg2
   print ("Inside the function : ", total)
   return total

total = sum2( 10, 20 )
print ("Outside the function : ", total )

print('-'*60)
############################################################
#Global vs. Local variables

total = 0   # global variable.

def sum3( arg1, arg2 ):
   total = arg1 + arg2 # Here total is local variable.
   #global total
   #total = arg1 + arg2
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum3( 10, 20 )
print ("Outside the function global total : ", total )

print('-'*60)
#######################################################



