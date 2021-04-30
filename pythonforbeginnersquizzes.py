#Python For Beginners Quizzes SoloLearn


#Basic Concepts Chapter 1

#Flight Time 

# You need to calculate the flight time of an upcoming trip. You are flying from LA to Sydney, covering a distance of 7425 miles, the plane flies at an average speed of 550 miles an hour.

# Calculate and output the total flight time in hours.

# Hint
# The result should be a float.
# Use the print statement to output the result.

distance = 7425
speed = 550
time = distance/speed
print(time)

#Output: 13.5





#Strings Chapter 2 

# Strings

# You need to make a program for a leaderboard.
# The program needs to output the numbers 1 to 9, each on a separate line, followed by a dot:
# 1.
# 2.
# 3.
# ...
# You can use the \n newline character to create line breaks, or, alternatively, create the desired output using three double quotes """.


for i in range (1,10):
    print('{:}'.format(f'{i}.'))

#Output 

#1.
#2.
#3.
#4.
#5.
#6.
#7.
#8.
#9.




#Variables Chapter 3


# Tip Calculator


# When you go out to eat, you always tip 20% of the bill amount. But who’s got the time to calculate the right tip amount every time? Not you that’s for sure! You’re making a program to calculate tips and save some time.

# Your program needs to take the bill amount as input and output the tip as a float.

# Sample Input
# 50

# Sample Output
# 10.0
# Explanation: 20% of 50 is 10.
# To calculate 20% of a given amount, you can multiply the number by 20 and divide it by 100: 50*20/100 = 10.0


def main():
    try:    
        bill = int(input())
        tip = bill*(20/100)
        print(tip)
    except:
        print("Please insert an integer next time")
        main()
main()
 


#input: 125 output: 25.0
#input: 268 output: 53.6







#Control Flow Chapter 4


# BMI Calculator


# Tracking your BMI is a useful way of checking if you’re maintaining a healthy weight. It’s calculated using a person's weight and height, using this formula: weight / height²

# The resulting number indicates one of the following categories:
# Underweight = less than 18.5
# Normal = more or equal to 18.5 and less than 25
# Overweight = more or equal to 25 and less than 30
# Obesity = 30 or more

# Let’s make finding out your BMI quicker and easier, by creating a program that takes a person's weight and height as input and outputs the corresponding BMI category.

# Sample Input
# 85
# 1.9

# Sample Output
# Normal
# Weight is in kg, height is in meters.
# Note, that height is a float.


weight = float(input(""))
height = float(input(""))
bmi = (weight/(height**2))

if bmi < 18.5:
   print("Underweight")   
elif (bmi >= 18.5 and bmi < 25):
   print("Normal")    
elif (bmi >= 25 and bmi < 30):
   print("Overweight") 
else:
   print("Obesity")  


#input 
#52  
#1.85   
#output Underweight
#input 
#130
#1.7
#output Obesity



#Lists Chapter 5 



# Sum of Consecutive Numbers


# No one likes homework, but your math teacher has given you an assignment to find the sum of the first N numbers.

# Let’s save some time by creating a program to do the calculation for you!

# Take a number N as input and output the sum of all numbers from 1 to N (including N).

# Sample Input
# 100

# Sample Output
# 5050

# Explanation: The sum of all numbers from 1 to 100 is equal to 5050.
# You can iterate over a range and calculate the sum of all numbers in the range.
# Remember, range(a, b) does not include b, thus you need to use b+1 to include b in the range.



N = int(input())


# Sum of natural numbers up to num num = 16 if num < 0: print("Enter a positive number") else: sum = 0 # use while loop to iterate until zero while(num > 0): sum += num num -= 1 print("The sum is", sum)# Sum of natural numbers up to num



if N < 0:
   print("Enter a positive number")
else:
   sum = 0
   # use while loop to iterate until zero
   while(N > 0):
    sum += N
    N -= 1
   print(sum)


#input 358
#output 64261

#input 12345
#output 76205685







#Functions Chapter 6 


# Search Engine


# You’re working on a search engine. Watch your back Google!

# The given code takes a text and a word as input and passes them to a function called search().

# The search() function should return "Word found" if the word is present in the text, or "Word not found", if it’s not.

# Sample Input
# "This is awesome"
# "awesome"

# Sample Output
# Word found
# Define the search() function, so that the given code works as expected.


text = input()
word = input()
    
if word in text:
    print("Word found")
else:
    print("Word not found")


#input 
#this is some sample text 
#some
#output Word found
#input 
#hi there
#friend
#output Word not found
