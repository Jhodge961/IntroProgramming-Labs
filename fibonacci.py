#CMPT 120
#Jason Hodge
#20 September 2018

Number = int(input("\nEnter n "))

n = 10
n1 = 0
n2 = 1
count = 0

if n <= 0:
   print("Enter a positive integer")
elif n == 1:
   print("Sequence upto",n,":")
   print(n1)
else:
   print("Sequence upto",n,":")
   while count < n:
       print(n1,end=' , ')
       nth = n1 + n2
       
       n1 = n2
       n2 = nth
       count += 1
       
