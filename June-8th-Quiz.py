import unittest
class Calculator :
    def add ( self , x , y) :
        return x + y
    def subtract ( self , x , y ) :
        pass
    def multiply ( self , x , y ) :
        pass
    def divide ( self , x , y ) :
        return x / y

class TestCalc ( unittest . TestCase ) :
    def setUp ( self ) :
        self . calc = Calculator ()
    def testAddNumbers ( self ) :
        self . assertEqual ( self . calc . add (3 , 2) , 5)
    def testAddLists ( self ) :
        List1=[1,2,3]
        List2=[4,5,6]
        for i in List1:
            for j in List2:
              self.assertEqual (self.calc.add(i,j),i+j)

if __name__ == "__main__":
    unittest.main()
# class B :
#     __instance = None
#     def __new__ ( cls ) :
#         if B . __instance is None :
#             B . __instance = object . __new__ ( cls )
#             return B . __instance
#     def __init__ ( self ) :
#         self . value = 1
# class A :
#     b = B ()
#     def __init__ ( self ) :
#         self . value = A . b . value
#         A . b . value += 1

# a1 = A ()
# a2 = A ()
# b1 = B ()
# a3 = A ()

# for instance in [ a1 , a2 , a3 , b1 ]:
#     print ( instance . value )