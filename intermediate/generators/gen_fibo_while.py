#def fibonacci(limit):       #Start with 0 1 1 2 3 5 8 13 ...
#    a,b=0,1
#    while a<limit:
#        yield a
#        a,b=b,a+b
#
#fib = fibonacci(int(input("Limite? ")))
#for i in fib:
#    print(i)
#
#
#
def fibo(limit):
    if limit<0:
        return("Please enter a positive integer")
    else:
        a,b=0,1
        count=0
        while count<limit:
            yield a 
            a,b = b, a+b
            count +=1 

fib = fibo(int(input("Cantidad valores fibonacci? ")))
for i in fib:
    print(i)



# Program to display the Fibonacci sequence up to n-th term

nvalues = int(input("Cual es el valor máximo? "))
n1, n2 = 0, 1
count = 0
if nvalues <= 0:
  print("Por favor ingresa un valor positivo")
elif nvalues == 1:
  print("Secuencia Fibonacci hasta",nvalues,":")
  print(n1)
else:
  print("Secuencia Fibonacci:")
  while count < nvalues:
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
