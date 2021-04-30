#These are 10 Python Quizzes given at the end of the Python 3 Course from SoloLearn.

#Solo Learn Course Python 3 - 1. Basic Concepts - Exponentiation

#Exponentiation is the raising of one number to the power of another. 
#This operation is performed using two asterisks **

#Let's use exponentiation to solve a known problem. 
#You are offered a choice of either $1.000.000 or $0.01(one penny) doubled every day for 30 days (the resulting amount is double every day). 

#Task:
#Write a program to calculate the amount that will result from the doubling to understand which choice reults ina larger amount.

#Hint 
#Let's see how exponentiation can be useful to perform the calculation. 
#For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).

#hint -> Use the print statement to output the resulting amount. 

result = 0.01*(2**30)
print(result)

#Your Output 
#10737418.24

#Expected Output 
#10737418.24


#Sololearn Python 3 Course - 2. Basic Concepts - Simple Calculator

#Simple calculator 

#Write a program to take two integers as input and output their sum. 

#sample input
#2
#8

#sample output 
#10

#hint -> Remember, input() results in a string.

a=int(input())
b=int(input())
sum = a + b
print(sum)


#SoloLearn Python 3 Course - 3. Control Structures - FizzBuzz

#FizzBuzz is a well known programming assignment asked during interviews. 

#The given code solves the FizzBuzz problem and uses the words "Solo" and "Learn" instead of "Fizz" and "Buzz".
#It takes an input n and outputs the numbers from 1 to n. 
#For each multiple of 3, print "Solo" instead of the number
#For each multiple of 5, prints "Learn" instead of the number
#For numbers which are multiples of both 3 and 5, output "SoloLearn".

#You need to change the code to skip the even numbers, so that the logic only applies to odd numbers in the range

#hint -> Remember, the continue statement can be used to skip a loop iteration. 


n = int(input())

for x in range(1,n):
    if x%2==0:
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
   
        
#Expected Output

#1
#Solo
#Learn
#7
#Solo
#11
#13


#SoloLearn Python 3 Course - 4. Functions & Modules - Celsius to Fahrenheit Converter

##Celsius to Fahrenheit 

#You are making a Celsius to Fahrenheit converter. 
#Write a function to take the Celsius value as an argument and return the corresponding Fahrenheit value.

#Sample Input 
#36

#Sample Output 
#96.8

#hint -> The following equation is used to calculate the Fahrenheit value: 9/5*celsius+32

celsius=int(input())

def conv(c):
    #your code goes here
    fahrenheit = (9/5 * celsius) + 32
    return(fahrenheit)
fahrenheit = conv(celsius)
print(fahrenheit)


#SoloLearn Python 3 Course - 5. Exceptions & Files - Book Titles


#You have been asked to make a special book categorization program, which assigns each book a special 
#code based on its title. 
#The code is equal to the first letter of the book, followed by the number of characters in the title.
#For example, for the book "Harry Potter", the code would be: H12, as it contains 12 characters
#(including the space).
#You are provided a books.txt file, which includes the book titles, each on written on a separate line. 
#Read the tile one by one and output the code for each book on a separate line. 

#For example, if the books.txt file contains:
#Some book
#Another book

#Your program should output:
#S9
#A12

#Recall the readline() method, which returns a list containing the lines of the file.
#Also remember that all lines, except the last one, contain a /n at the end, which should not 
#be included in the character count. 

#Expected output 
#H12
#T16
#P19
#G18

file = open("/usercode/files/books.txt", "r")

for line in file:
	title=line.replace('\n','')
	count=len(title)
	print(f'{title[0]}{count}')
file.close()

#another way would be 

#file = open("/usercode/files/books.txt", "r")
#for line in file.readlines():
#    print(f'{line[0]}{len(line.strip())}')
#file.close()


#SoloLearn Python 3 Course 6. More Types - Longest Word


#Given a text as input, find and output the longest word. 

#Sample Input
#this is an awesome text 

#Sample Output
#awesome

#hint 
#Recall the split('') method, which returns a list of words of the string. 

txt=input()

#Finding the longest word 

longest=max(txt.split(), key=len)

#Displaying longest word

print(longest)

#Input 
#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua

#Expected output 
#consectetur



#SoloLearn Python 3 Course - 7. Functional Programming - Fibonacci


#The Fibonacci sequence is one of the most famous formulas in mathematics. 
#Each numer in the sequence is the sum of the two numbers that precede it. 
#For example, here is the Fibonacci sequence for 10 numbers, starting from 
#0: 0, 1, 1, 3, 5, 8, 13, 21, 34. 

#Write a program to take N (variable num in code template) positive numbers as 
#input, and recursively calculate and output the first N numbers of the FIbonacci
#sequence (starting from 0).

#Input 
#5

#Expected output 
#0
#1
#1
#2
#3


#If you are making the Fibonacci sequence for n numbers, you should use n<=1 
#condition as the base case.


def fibonacci(n):
    
    if n<=1:
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))
        
nterms=int(input())

if nterms<=0:
    print ("Enter a positive integer")
else: 
    for i in range(nterms):
        print(fibonacci(i))
    
    
#Solo Learn Course Python 3 - 8. OOP - Juice Maker

#You are given a Juice class, which has name and capacity properties. 
#You need to complete the code to enable and adding of two Juice objects, resulting in a new Juice object with the combined capacity and name of the two juices being added. 
#For example, if you add an Orange juice with 1,0 capacity and an Apple juice with 2.5 capacity, the resulting juice should have: 
#name: Orange&Apple
#capacity: 3.5

#The names have been combined using an & symbol

#hint 
#Use the __add__ method to define a custom behavior for the + operator and return
#the resulting object. 

class Juice:
    def __init__(self, name, capacity):
        self.name=name
        self.capacity=capacity 
    def __str__(self):
        return (self.name + '('+str(self.capacity)+'L)')
        
    def __add__(self, other):
        return Juice(self.name + '&' + other.name, self.capacity + other.capacity)
        
a = Juice('Orange', 1.5)
b = Juice('Apple', 2.0)

result = a + b
print(result)

#Expected Output 
# Orange&Apple (3.5L)



#Solo Learn Course Python 3 - 9. Regular Expressions - Phone Number Validator

##You are given a number input, and need to check if it is a valid phone number. 
#A valid phone number has exactly 8 digits and starts with 1,8 or 9. 
#Output "Valid" if nuber is valid and "invalid", if it is not. 

#Sample input 
#81239870

#Sample output 
#Valid 

#You can use a regular expression to check if the input matches the given pattern.

import re 
#your code goes here
num = int(input())
if (len(str(num))==8 and int(str(num)[0])==1 or int(str(num)[0])==8 or int(str(num)[0])==9):
    print("Valid")
else:
    print("Invalid")
    
    
#Tese case #1

#Input 
#81234567

#Output
#Valid

#Expected Output
#Valid

#Test case #2
#Input 
#57345672

#Yout Output 
#Invalid

#Expected Output
#Invalid


#Solo Learn Course Python 3 - 10. Pythonicness and Packaging - Adding Words

##You need to write a function that takes multiple words as its argument and returns a concatenated version of those words separated by dashes (-). The function should be able to take a varying number of words as the argument. 

#Sample input
#this
#is
#great

#Sample Output 
#this-is-great

#Recall, using *args as a function parameter enables you to pass an arbitrary number of arguments to that function

#Expected Output 
#I-love-Python-!

#Either code works 


#l = ['I', 'love', 'Python', '!']
#s = '-'.join(l)
#print(s)


def l(*argv): 
    for arg in argv: 
        print (arg)
l = ('I', 'love', 'Python', '!')
print('-'.join(l))












