def decorators(fun):
 def deno(n1,n2):
     if n1<n2:
         n1,n2=n2,n1
     return fun(n1,n2)
 return deno

@decorators
def div(n1,n2):
      return  n1//n2

n1=int(input("Enter two numbers"))
n2=int(input("Enter two numbers"))
print(n1,n2)


print(div(n1,n2))