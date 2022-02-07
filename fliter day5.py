from unittest import result


happy=list(range(1,50))
result3=list(filter(lambda x: (x%3==0),happy))
result5=list(filter(lambda x: (x%5==0),happy))

print("This num only divisible  by 3 ",result3)
print("this num only divisible by 5",result5)