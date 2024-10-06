# printing my name using the print function from python
print('shamsa')
print('hello')
# The input function prompts the user for input
name = input('what is your name? ')
print('helloo '+name)
# Fundamental Data types 
int
float
bool
str
list
tuple
set
dict

#Classes- custom types (Under this, you can create a class and name it whatever you want)

#Specialized Data Types(Extensions that can be added)

None

#Intergers (Int) are numbers, can be used on mathematical operations 
print(2+4)
print(2-4)
print(2*4)
print(2/4)

#How to find the data type of an interger
print(type(2+4))
print(type(2-4))
print(type(2*4))
print(type(2/4)) # 0.5

#Float (Is a floating point number (a number with decimal points)

#Double multiply 
print(2 ** 2)  #2 squared 2

#Double Division (Rounds up to an interger)
print(2 // 4)
print(5 // 4)

#Module (Take the reminder of the number)
print(6 % 4)
print(5 % 4)
#math fuctions
#Round - means rounding off to the nearest number 
print(round(3.1))

#abs- returns the absolute value of the number meaning no negative value
print(abs(-20))

#operator precedence
print((20-3) + 2** 2)

#Order to follow
# ()
# **
# * /
# + -

#Complex
# There is another data type known as complex. - usually a complex number. its neither float nor int
complex

#Binary - bin
#bin5- this is a binary representation of 5. (binary are 0,1)

#changing binary to int (Havent understood the base thing )
print(int('0b101', 2))

# for instance, my iq is 190 so
iq = 190
# so iq becomes the variable name 
print(iq)

#Variables

#CONSTANTS - these are constant numbers and are usually in capital letters
PI = 3.14

# Dont change thoroughout the usage
# Though to change them, 

PI = 0

#assign values to a variable 
a,b,c = 1,2,3
print(a)
print(b)
print(c)

# Expressions  - a piece of code that produces a value
# e.g iq/5 is an expression

iq = 100
user_age = iq/5
print(user_age)

# A statement is an entire line of code that performs an action 
# user_age = iq/5 and iq = 100 is also another statement 


# Augmented assignment operator (short form for additions , subtraction and multiplication)
some_value = 5
some_value -= 2
some_value += 2
some_value *= 2

#The above is the same as  saying some_value = some_value + 2

# 3. Data type - String 
# A string is like a text or sentence 
# A string has to be in "" or ''
# So to get the type of class, yo go by 
type('hi hello there 24!')

# So to view thw results yo go by print(type('hi hello..........'))

print(type('hi hello there 24!'))


# Long_string - this is used for long texts and uses ''' (3 quotes)

long_string = '''
wow
0 0
---
'''

print(long_string)

# Adding up names 

first_name = 'Andrei'
last_name = 'Neagoie'
full_name = first_name + last_name 
# But if we print full name, the names will be joined so we add ' ' for space e.g

full_name = first_name + ' ' + last_name
print(full_name)

# Strings concatenation - means adding strings 
'hello'+ 'Andrei'
print('hello' + 'Andrei')

#Type conversion 
#changing from one type to another
# so str(100)- 100 is an interger but we can check and see the type that is now 
print(type(str(100)))

# so to change back to int we can go like
print(type(int(str(100))))

#Escape sequence - Use escape sequence for apostrophe
# for example, you want to write that the weather is sunny
# weather = 'It's sunny' you go by...

weather = "It's sunny"
# so now if we want to add "kind of "
# so saying weather "It's "kind of" sunny" is wrong 
# Instead we use \ - recongnizes that whatever comes after it should remain as it is 

weather = "It\'s \"kind of\" sunny "
print(weather)

# So \t - means tab and also \n means a new line 

#formatted strings 
name = 'johnny'
age = 55

print(f'hi {name}. you are {age} years old')

# String index / slicing
# [start:stop:stepover]
selfish = '01234567'
            #01234567
print(selfish[1:])
print(selfish[0:4])
print(selfish[0:8:1]) # stepover - this by default goes one by one

# so  in python, a (- sign) means start from the end of the string 
# so 
print(selfish[-3])
print(selfish[-2])
print(selfish[-1])
print(selfish[::-1])    #default from behind- usually used, if you want to reverse 
print(selfish[::-2])


#
# [] square blankets can help you acess diff parts of a string 
# Immutiablity - Strings in python are immutiable - they cant be changed 
# You can re -assign a string once created. but you can change it and create another string 
# e.g 
selfish = '01234567'

# so you cant just change 01234567 to 8 but 

selfish = selfish + '8'

print(selfish)

#Built -in fuctions + methods
# str has len meaning length od a word - counts words

print(len('helllloooo'))

quote = 'to be or not to be'

print(quote.upper())  # change the text to upper case
print(quote.capitalize()) # change the 1st letter to capital letter 
print(quote.find ('be'))
print(quote.replace('be', 'me'))

#Booleans 
#bool - #use true and false 

name = 'Andrei'

is_cool = False

is_cool = True 

print(bool(1))

# In bool, 1 is true then 0 is false 

print(bool(0))

# Lets create a program that guesses your age

birth_year = input('what year were you born?')

age = 2024 - int(birth_year)

print(f'your age is:{age}')

# count the number of words #

#array

#range 

# With an f string, you can add python expressions in the sentence 
# Password checker

username = input('What is your name?')
password = input('What is your password?')

password_length = len(password)
password_hidden = ('*'* password_length)

print(f'{username} your password, {password_hidden} is {password_length} letters long')

# Data type - List
# List are noted by []

li = [1,2,3,4,]
li2 = ['a', 'b', 'c']
li3 = [1,2,'a', True]

# Add something something new to the list 

Add = li . append['good']

#In python, list are a form of array

#Data Structure - A container that has all our data - so the [] help us collect different data types 



# List slicing 

amazon_cart = [
    'notebooks', 
    'sunglasses',
    'toys',
    'grapes'

]

print(amazon_cart[0])
print(amazon_cart[1])

print(amazon_cart[0:1])

#Lists are changeable 

amazon_cart[0] = 'laptop'
print(amazon_cart)

# [:] to copy the list - this brings back the original list 
new_cart = amazon_cart[:]####--more explanation 
print(new_cart)

#Matrix 
# Is an array with another array inside it
matrix =[
    [1,2,3]
    [2,4,6]
    [1,5,7]
]

# accessing the 1st itmem (array)and also accessing the 1st item in that lsit  

print(matrix[0][1])

#List methods

basket = [1,3,4,5]

# adding
basket = basket.append(100)
print(basket)

#Insert -modifies a list in place 
basket.insert(5,100)

#extend- its like adding multiple values to the list 

basket= basket.extend([100, 1001])

#removing
basket.pop() - #pop means removing whatever is at the end of the list
print(basket)

basket.remove(2)- #so with remove, we give it the exact value that we want to remove
# so in that case, 2 will be removed

#clear- clear removes whatever is in the list
new_list = basket.clear()

# it wont return a new list but it will clear the whole basket so 

print(basket)

#index- index(value, start , stop)-more explanation  on index

basket = ['a','b','c','d']


print(basket.index('c'))

#Python key words


#in- can be used for example print('b'in basket)
print('b'in basket)

#Count- counts how many times an item occurs in  the list 
print(basket.count('d'))


#sort - sorting in order 

basket = ['a', 'c','x','d']
basket.sort
print(basket)

#reverse
basket.reverse()
print(basket)

#range 
print(range(1,100))
print(list(range(1,100))) #its going to give a list from 1 to 99

# .join()- usually used on strings
# forexample - given sentence ' ' and you want to join the following words- ('hi', 'my', 'name', 'is', 'JoJo') so

new_sentence = ' '.join('hi', 'my', 'name', 'is', 'JoJo')
print(new_sentence)

#list unpacking - assigning a variable to a value 

a,b,c = [1,2,3]
print(a)
print(b)
print(c)


a,b,c, other, d = [1,2,3,4,5,6,7,8,9]
print(other)
print(d)

#None 
weapons = None
print(weapons)

#Dictionary - a dictionary is unordered key value pair

dictionary = {
    'a': 1,
    'b': 2
}
print(dictionary['a'])

#how to avoid errors
# .get 
print(dictionary.get('age'))

#how to use a default value 
print(dictionary.get('age',55)) - #here it says that incase age dosent exist, use 55 as a default value 

#Dictionaty methods

#Tuple



