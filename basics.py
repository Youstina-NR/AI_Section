print("Hello, World!")
#print("This is a
#multiline string.")
print("""This is a
multiline string.""")

print('-'*50)
########################################################
#Multi-Line Statements
x1 = 1 ; x2 = 3; x3 = 5  #The semicolon ( ; ) allows multiple statements on a single line
total = x1 + \
   x2 + \
   x3
########################################################
#Multiple Assignment
a = b = c = 1
print(a)
print(b)
print(c)
a,b,c =1,2,"john"
print(a,b,c)
print(a,b,c,sep='/')

print('-'*50)
########################################################
#Casting
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
print(x,y,z)
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
print(x,y,z)
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
print(x,y,z)

print('-'*50)
########################################################
#String
str = 'Hello World!'

print (str)          # Prints complete string
print (str[0])       # Prints first character of the string (index 0)
print (str[2:7])     # Prints characters starting from index 2 to index 6 ( [2:7) )
print (str[2:])      # Prints string starting from 3rd character
print (str[:2])      # Prints first two characters
print (str * 2)      # Prints string two times
print (str + "TEST") # Prints concatenated string

a = " Hello, World! "
print(a.strip()) #strip() method removes any whitespace from the beginning or the end
print(len(a))
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
print(a.replace("l","x",2))
print(a.split(",")) # returns ['Hello', ' World!']
#split() method splits the string into substrings if it finds instances of the separator

print("Enter your name:")
x = input()
print("Hello, " + x)

print('-'*50)
########################################################
#Arithmetic Operators
# + - * / % ** //
# **    Exponentiation	x ** y	 
# //	Floor division  x // y
#Assignment Operators
# = += -= *= /= %= //= **=
# &= |= ^= >>= <<=
#Comparison Operators
# == != > < >= <=
#Logical Operators
# and or not
# not(x > 5 and x < 10)
x = 5
if x > 0 :
  print('+ve')
elif x < 0 :
  print('-ve')
else :
  print('zero')

#Identity Operators
# is       Returns true if both variables are the same object
# is not   Returns true if both variables are not the same object
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x 

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have thew same content

print(x == y)
# returns True because x is equal to y


x[0] = "orange"
print(x)
print(z)
z=x[:]
print(x is z)
z[0] = "apple"
print(x)
print(z)

#Membership Operators
# in        Returns True if a sequence with the specified value is present in the object
# not in
print("banana" in x)

#Bitwise Operators
# & | ^ ~ << >>
x = 3
y = 5
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x>>1)
print(y<<2)

print('-'*50)
########################################################
#List
List = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (List)          # Prints complete list
print (List[0])       # Prints first element of the list
print (List[-1])      # prints last element of the list
print (List[1:3])     # Prints elements starting from 2nd till 3rd 
print (List[2:])      # Prints elements starting from 3rd element
print (tinylist * 2)  # Prints list two times
print (List + tinylist) # Prints concatenated lists

print (List[::1])
print (List[::-1])
print (List[::2])
print (List[::-2])
print (List[1::2])

List[0] = 222
print (List)

for x in List:
  print(x)

for i in range(0,len(List)):
  print(List[i])
  
print(len(List))

List.append("orange")
print(List)

List.insert(1, "orange")
print(List)

List.remove("orange") 
#  remove first match 
print(List)

List.pop()  
# last element
print(List)

List.pop(0)
print(List)

del List[0]
print(List)

List.clear()
print(List)
List.append(1)
del List
#print(List)
#List.append(2)

#list() Constructor

thislist = list(["apple", "banana", "cherry"])
print(thislist)

print(thislist.count("apple"))

cars = ['Ford', 'BMW', 'Volvo']
thislist.extend(cars)
print(thislist)

points = [1, 4, 5, 9]
thislist.extend(points)
print(thislist)

x = thislist.index("cherry")
print(x)

thislist.reverse()
print(thislist)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
cars.sort(reverse=True, key=myFunc)
print(cars)

L = [3,5,1,7,9,0]
print(min(L))
print(max(L))
print(sum(L))

import numpy as np
L= [1,2,1,3,1]
print(list(np.unique(L)))

print('-'*50)
########################################################
#Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print(dict)
print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values


dict = {"b":1.2,"a":3.5,"c":4}

for x in dict:
  print(x)

for x in dict:
  print(dict[x])

for x in dict:
  print(x,' : ',dict[x])

for x, y in dict.items():
  print(x," : " ,y)


print('-'*50)
########################################################




