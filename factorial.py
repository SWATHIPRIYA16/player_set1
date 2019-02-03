num=input()
factorial = 1
if num == 0:
   print("1")
else:
   for i in range(1,int(num) + 1):
       factorial = factorial*i
   print(factorial)
