from itertools import product
from tokenize import Number


#define a function which will taLk a number as argument and return its factorial

number=int(input("enter no:"))
def factorial_iem(number):
     product=1
     for i in range(number):
            product =product*(i+1)
     return product
        
f=factorial_iem(number)
print(f)