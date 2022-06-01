# Yousef Ibrahim Gomaa Mahmoud - ID: 320210207 - Section 10

# Problem 1

# class Person:
#     def __init__(self, First, Last, Age):
#         self.firstname = First
#         self.lastname = Last
#         self.age = Age

# class Teacher(Person):
#     def __init__(self, First, Last, Age, Dpt):
#         Person.__init__(self, First,Last,Age)
#         self.department = Dpt
#         self.courses = []

#     def add_course(self, course):
#         self.courses.append(course)

#     def get_teacher_info(self):
#         print("Teacher Information of", self.firstname,self.lastname)
#         print("---------------\n","Name:",self.firstname,self.lastname+"\n","Department:",self.department+"\n",
#         "Courses:",self.courses)
#         print("---------------\n")

        
# class Student(Person):
#     def __init__(self, First, Last, Age, GPA, Supervisor):
#         Person.__init__(self, First,Last,Age)
#         self.GPA = GPA 
#         self.courses = []
#         self.SV = Supervisor

#     def add_course(self, course):
#         self.courses.append(course)
    
#     def print_info(self):
#         print("Student Information of",self.firstname,self.lastname)
#         print("---------------\n","Name:",self.firstname,self.lastname+"\n","GPA:",str(self.GPA)+"\n",
#         "Supervisor:",self.SV+"\n","Courses Taken:",self.courses)
#         if (self.GPA >= 3.5):
#             print("Grade: Excellent")
#         elif (self.GPA < 3.5 and self.GPA >= 3.0):
#             print("Grade: Very Good")
#         elif (self.GPA < 3.0 and self.GPA >= 2.5):
#             print("Grade: Good")
#         elif (self.GPA < 2.5 and self.GPA >= 2.0):
#             print("Grade: Passed")
#         else:
#             print("Grade: Failed")
#         print("---------------\n")

# Teacher1 = Teacher("Yousef","Ibrahim","25","Computer Science")
# Teacher1.add_course("Advanced Programming")
# Teacher1.add_course("Data Structure & Algorithms")
# Teacher1.get_teacher_info()

# Student1 = Student("Yousef","Ibrahim","25",3.6,"Ashraf")
# Student1.add_course("Advanced Programming")
# Student1.add_course("Data Structure & Algorithms")
# Student1.print_info()

# Problem 2

# import unittest

# def Add(arg):
#     total = 0
#     for val in arg:
#         total += val
#     return total

# class TestSum(unittest.TestCase):
#     def test_list_int(self):
#         args = [5,4,1,6]
#         self.assertEqual(Add(args),16)

#     def test_list_fraction(self):
#         args = [0.5,1/4,0.6667]
#         self.assertEqual(Add(args),1.4167)

#     def test_bad_type(self):
#         args = [3,"Str",0.7]
#         self.assertRaises(TypeError,Add,args)

# if __name__ == '__main__':
#      unittest.main() 

# Problem 3
import doctest

def digits_only(s):
    '''
    >>> digits_only("Jk3lolx51#%")
    351
    >>> digits_only("Hi4!x3")
    43
    '''
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    output = ""
    for num in s:
         if num in numbers:
            output += num
    return int(output)

if __name__ == '__main__':
    doctest.testmod(verbose=True)
 