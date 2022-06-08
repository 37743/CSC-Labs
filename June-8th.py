# Yousef Ibrahim Gomaa Mahmoud - ID: 320210207 - Section 10

# 1.Write a list comprehension that enumerates the odd squares of the integers 1 through 20
# inclusive. 
# ----------
list1 = [x*x for x in range(1,21) if x*x % 2 != 0] 
print("Problem 1 output:",list1)

# 2.Write a list comprehension statement to generate a list of all pairs of odd positive integer
# values less than 10 where the first value is less than the second value.
# ----------
list2 = [[x,y] for x in range(1,10) for y in range(1,10) if (x%2 != 0 and y%2 != 0) and (x>y)] 
print("Problem 2 output:",list2)

# 3.Write a one-line expression that computes the sum of the first 10 odd square numbers
# (starting with 1).
# ----------
print("Problem 3 output:",sum([n*n for n in range(1,11) if n*n % 2 != 0],0))

# 4.Write a lambda function to calculate the power of 2 of elements inside a list.
# ----------
print("Problem 4 output:",list(map(lambda i: i**2,[1,2,3,4,5])))

# 5.Given an array A of non-negative integers, return an array consisting of all the even elements
# of A, followed by all the odd elements of A.
# ----------
A = [1,2,3,4,5,6,7,8,9,10] # Example Array A
print("Problem 5 output:",[x for x in A if (x%2 == 0)] + [x for x in A if (x%2 != 0)])

# 6.Use map to generate a new list where all values are replaced by their absolute values. You
# don’t need to use a lambda function.
# ----------
print("Problem 6 output:",list(map(abs,[-5,-7,10,-20,106,-204])))

# 7.Use map and a lambda function to convert a list of Fahrenheit temperatures to a list of
# Celsius temperatures.
# ----------
FahrenheitList = [100,125,150,175,200,225,250]
print("Problem 7 output:",list(map(lambda x: (x-32)/1.8,FahrenheitList)))

# 8.Use map and a lambda function to find the maximum x coordinate (the 0-th coordinate) in a
# list of points.
# ----------
PList = [[1,2],[2,7],[-1,8],[9,3],[1,5],[-7,10]]
print("Problem 8 output:",max(list(map(lambda x: x[0],PList))))