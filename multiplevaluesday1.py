#Multiple values as input and Print the sum
x= [int(i) for i in input('Enter the values:').split()]
s=0
for j in x:
    s += j 
    print(s)
