###########################################################################################################################################
# CLASSES AND OBJECT EXPLORATION
###########################################################################################################################################

class A:
    def __init__(self, c):
        print('---------Inside class A----------')
        self.c = c
    print('Print inside A.')

    def alpha(self):
        c = self.c + 1
        return c


print(dir(A))
print('Instantiating A..')
a = A(1)
print(a.alpha())


class B:
    def __init__(self, a):
        print('---------Inside class B----------')
        self.a = a

    print(a.alpha())
    d = 5
    print(d)
    print(a)


print('Instantiating B..')
b = B(a)
print(a)

'''
Algorithmically we can view the program consisting of the following:
1. Class definition of A
  1.1 Constructor for A
  1.2 Definition of local method alpha()
2. Instantiating object a over class A
3. Calling method alpha() over object of class A
4. Class definition of B
5. Constructor for B
  5.1 Calling method alpha() over object of class A
  5.2 Instantiating object a over class B *.
Additional print statements distributed through the code.
'''
