#wtite a program to check whether the given number is prime or not using functions
num = int(input("Enter a number: "))
def prime(num):
    if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               print(num,"is not a prime number")   
               break  
       else:  
           print(num,"is a prime number")  
             
    else:  
       print(num,"is not a prime number")
prime(num);