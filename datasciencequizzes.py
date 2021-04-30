#Python Data Science SoloLearn Course Quizzes


#Data Manipulation Chapter 1 

#Data Science - Average of Rows


#In a matrix, or 2-d array X, the averages (or means) of the elements of rows is called row means.

#Task
#Given a 2D array, return the rowmeans.

#Input Format
#First line: two integers separated by spaces, the first indicates the rows of matrix X (n) and the second indicates the columns of X (p)
#Next n lines: values of the row in X

#Output Format
#An numpy 1d array of values rounded to the second decimal.

#2 2
#1.5 1
#2 2.9

#Sample Output
#[1.25 2.45]
#Explanation
#The first row has two numbers 1.5 and 1, thus the sum is 1.5 + 1 = 2.5 and the mean is then 2.5/2 = 1.25. Then for the second row, the average is calculated as (2 + 2.9)/2 = 4.9/2 = 2.45.



import numpy as np
n, p = [int(x) for x in input().split()]
lst = []
for i in range(n):
    lst.append(input().split())
print(np.array(lst).astype(np.float).mean(axis=1).round(2))



#input 
#2 2 
#1.5 1
#2 2.9

#output [1.25 2.45]

#input 
#3 2
#1 2
#1 0.5
#1 0.3

#output [1.5  0.75 0.65]







#Data Analysis Chapter 2 



#Data Science - Reshape
'''

Task
Given a list of numbers and the number of rows (r), reshape the list into a 2-dimensional array. Note that r divides the length of the list evenly.

Input Format
First line: an integer (r) indicating the number of rows of the 2-dimensional array
Next line: numbers separated by the space

Output Format
An numpy 2d array of values rounded to the second decimal.

Sample Input
2
1.2 0 0.5 -1

Sample Output
[[ 1.2 0. ]
[ 0.5 -1. ]]
Explanation
The required number of the rows is 2, and we are given a list of 4 numbers; as a result the 2d array should be 2 x 2. So the first row is the first two number and the second row contains the next two numbers in given list.
'''

import numpy as np
r = int(input()) 
lst = [float(x) for x in input().split()]
arr = np.array(lst)
arrshaped = arr.reshape(r, int(len(lst)/r))
print(arrshaped)


#input 
#2 
#1.2 0 0.5 -1

#output 
#[[ 1.2  0. ]
# [ 0.5 -1. ]]


#input 
#3 
#1 2 1 0.5 1 0.3

#output 
#[[1.  2. ]
# [1.  0.5]
# [1.  0.3]]










#Data Visualization Chapter 3 



'''
Data Science - Missing Numbers


Imputing missing values.

In the real world, you will often need to handle missing values. One way to impute (i.e., fill) the numerical column is to replace the null values with its mean.

Task
Given a list of numbers including some missing values, turn it into a pandas dataframe, impute the missing values with the mean, and finally return the dataframe.

Input Format
A list of numbers including one or more string "nan" to indicate a missing value.

Output Format
A list of imputed values where all values are rounded to its first decimal place.

Sample Input
3 4 5 3 4 4 nan

Sample Output
0 3.0
1 4.0
2 5.0
3 3.0
4 4.0
5 4.0
6 3.8
dtype: float64
Explanation
The mean of 3, 4, 5, 3, 4, and 4 is 3.8, so we replace the missing value with the mean.
PY
'''


import numpy as np

lst = [float(x) if x != 'nan' else np.NaN for x in input().split()]

import pandas as pd
df = pd.Series(lst)
#df = pd.DataFrame(lst)
df = df.fillna(df.mean())
df = df.round(decimals = 1)
print(df)



#input 
#3 4 5 3 4 4 nan


#output
#0    3.0
#1    4.0
#2    5.0
#3    3.0
#4    4.0
#5    4.0
#6    3.8
#dtype: float64




#input 
#nan 20 22 nan 25 28 20 23

#output 
#nan 20 22 nan 25 28 20 23










#Linear Regression Chapter 4 


'''
Data Science - Ordinary Squares


Ordinary least squares for linear regression.

Ordinary least squares (OLS) is a method to estimate the parameters β in a simple linear regression, Xβ = y, where X is the feature matrix and y is the dependent variable (or target), by minimizing the sum of the squares of the differences between the observed dependent variable in the given dataset and those predicted by the linear function. Mathematically, the solution is given by the formula in the image, where the superscript T means the transpose of a matrix, and the superscript -1 means it is an inverse of a matrix.

Task
Given a 2D array feature matrix X and a vector y, return the coefficient vector; see the formula.

Input Format
First line: two integers separated by spaces, the first indicates the rows of the feature matrix X (n) and the second indicates the columns of X (p)
Next n lines: values of the row in the feature matrix
Last line: p values of target y

Output Format
An numpy 1d array of values rounded to the second decimal.

Sample Input
2 2
1 0
0 2
2 3

Sample Output
[2. , 1.5]
Explanation
The feature matrix X has n = 2 rows and p = 2 features. Following the OLS solution, substitute X by np.array([[1. 0.], [0. 2.]] and y by np.array([2. 3.]), respectively, performing the matrix multiplication using tools in numpy results in np.array([2. 1.5]).
'''

n, p = [int(x) for x in input().split()]
X = []
for i in range(n):
    X.append([float(x) for x in input().split()])

y = [float(x) for x in input().split()]


import numpy as np
X=np.array(X).reshape(n,p)
y=np.array(y)
b=np.linalg.pinv(X) @ y.transpose() #beta
print(np.around(b,decimals=2))


'''

Input
2 2
1 0
0 2
2 3
Output
[2.  1.5]


Input
3 2
1 2
1 0.5
1 0.3
3 3.5 3.2
Output
[ 3.42 -0.2 ]

'''








#Classification Chapter 5


'''

Data Science - Binary Disorder


Confusion matrix of binary classification.

For binary classifications, a confusion matrix is a two-by-two matrix to visualize the performance of an algorithm. Each row of the matrix represents the instances in a predicted class while each column represents the instances in an actual class.

Task
Given two lists of 1s and 0s (1 represents the true label, and 0 represents the false false) of the same length, output a 2darrary of counts, each cell is defined as follows

Top left: Predicted true and actually true (True positive)
Top right: Predicted true but actually false (False positive)
Bottom left: Predicted false but actually true (False negative)
Bottom right: Predicted false and actually false (True negative)

Input Format
First line: a list of 1s and 0s, separated by space. They are the actual binary labels.
Second line: a list of 1s and 0s, the length is the same as the first line. They represented the predicted labels.

Output Format
A numpy 2darray of two rows and two columns, the first row contains counts of true positives and false positives and the second row contains counts of false negatives and true negatives.

Sample Input
1 1 0 0
1 0 0 0

Sample Output
[[1., 0.],
[1., 2.]]
Explanation
Among the actual labels, there are 2 trues and 2 falses. One true label was correctly predicted as true and the other was incorrectly predicted as false; that is, one true positive and one false negative. Of the two false labels, both were correctly predicted; that is, zero false positive and two true negatives.
'''


y_true = [int(x) for x in input().split()]
y_pred =  [int(x) for x in input().split()]


from sklearn.metrics import confusion_matrix
print((confusion_matrix(y_pred, y_true, labels=[1, 0]))/1)



'''
Input
1 1 0 0
1 0 0 0
Your Output
[[1. 0.]
 [1. 2.]]
 
 
 Input
1 0 0 1
1 0 0 0
Your Output
[[1. 0.]
 [1. 2.]]
 '''











#Clustering Wines Chapter 6


'''
Data Science - Pandas Pandas Pandas


Finding the next centroid

Unsupervised learning algorithm clustering involves updating the centroid of each cluster. Here we find the next centroids for given data points and initial centroids.

Task
Assume that there are two clusters among the given two-dimensional data points and two random points (0, 0), and (2, 2) are the initial cluster centroids. Calculate the euclidean distance between each data point and each of the centroid, assign each data point to its nearest centroid, then calculate the new centroid. If there's a tie, assign the data point to the cluster with centroid (0, 0). If none of the data points were assigned to the given centroid, return None.

Input Format
First line: an integer to indicate the number of data points (n)
Next n lines: two numeric values per each line to represent a data point in two dimensional space.

Output Format
Two lists for two centroids. Numbers are rounded to the second decimal place.

Sample Input
3
1 0
0 .5
4 0

Sample Output
[0.5 0.25]
[4. 0.]
Explanation
There are 3 data points and we would like to identify two clusters among them. Initial centroids are given (0, 0), and (2, 2). The distances between the first data point (1, 0) and each of the centroids are 1.0 and 2.24, rounded to the second decimal place. The first data point is closter to (0, 0), thus assigned the 0-th cluster. Similarly data point (0, .5) is closer to (0, 0) than to (2, 2), also assigned to the 0th cluster; while (4, 0) is closter to (2, 2), thus assigned to the 1st cluster. To calculate the new centroids, take the mean of all data points in the 0-th and 1st cluster, respectively. Hence the results are [0.5 0.25] and [4. 0.].
'''



n = int(input())

import numpy as np 

X=[]
for i in range(n):
    X.append([float(x) for x in input().split()])


x1 = np.array([0, 0])
x2 = np.array([2, 2])

X=np.array(X)
a=[]
b=[]
for i in range(n):
    if np.sqrt(((X[i]-x1)**2).sum()) <= np.sqrt(((X[i]-x2)**2).sum()):
        a.append(X[i])
    elif np.sqrt(((X[i]-x1)**2).sum()) > np.sqrt(((X[i]-x2)**2).sum()):
        b.append(X[i])

a=np.array(a)
b=np.array(b)

sum_a_1=0
sum_a_2=0
sum_b_1=0
sum_b_2=0



for i in range(len(a)):
    sum_a_1+=a[i][0]
    sum_a_2+=a[i][1]

for i in range(len(b)):
    sum_b_1+=b[i][0]
    sum_b_2+=b[i][1]



if (len(a)!=0):
    sum_a_1/=len(a)
    sum_a_2/=len(a)
    sum_a_1 = sum_a_1.round(2)
    sum_a_2 = sum_a_2.round(2)
if (len(b)!=0):
    sum_b_1/=len(b)
    sum_b_2/=len(b)
    sum_b_1 = sum_b_1.round(2)
    sum_b_2 = sum_b_2.round(2)




c=[]
c.append(sum_a_1)
c.append(sum_a_2)
d=[]
d.append(sum_b_1)
d.append(sum_b_2)

c=np.array(c)
d=np.array(d)

if len(a)==0:
    print(None)
else:
    print(c)

if len(b)==0:
    print(None)
else:
    print(d)



'''
Input
3
1 0
0 .5
4 0
Your Output
[0.5  0.25]
[4. 0.]




Input
4
1 0
0 1
1 1
2 2
Your Output
[0.67 0.67]
[2. 2.]
'''









