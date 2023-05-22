def even_numbers():
    x = range(10)
    for i in x:
        if i%2==0:
            print(i)

def divisible_by_five():            
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
    else:
        print(f"{i} is not divisible by 5") 


def multiple_comparison():            
    x = range(50)
    for i in x:
        if i%5==0:
            print(f"{i}is divisible by 5")
        elif i %7 == 0:
            print(f"{i} is divisible by 7") 
        elif i %9 == 0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is not divisible by 5,7 or 9")


def add_or_even():
    x = range(20)
    for i in x:
        if i%2 == 0 and i%3==0:
            print(f"{i}is divisible by both 2 and 3")
        elif i %2 == 0 or i% 3==0:
            print(f"{i} is divisible by either 2 or 3") 
        else:
            print(f"{i} is not divisible by either 2 or 3")   

def while_loop():
    x = 1
    while x < 10:
        print("Hello")
        x+=1
       

def break_statement():
    x = 1
    while x<10:
        print("Hello")
        x+=1
        if x == 5:
            break

def continue_statement():
    x= 0
    while x <= 20:
        x+=1
        if x % 3 == 0:
           continue
        print(x) 

                                                                    #Test Qsns

#Qsn 1) Write a function that uses while, if and continue statements
      #  to print all the even numbers between 0 and 50. 

def even_numbers():
    y = 0
    while y <= 50:
        if y % 2 !=0:
           y+=1
           continue
        print(y)
        y += 1

even_numbers()        
                     

#Qsn  2)Write a function that takes an integer argument and prints 
      # "Prime" if the number is prime, and "Not prime" if the number is not prime.

def number_is_prime(int):
    k = 69
    if k>1:
        for i in range (2,int (k/2)+1):
            if k %i == 0:
                print(k, "is not prime")
    else:
        print(k,"is prime")
number_is_prime(int)        
        

#Qs n3) Write a function that takes a list of integers as input and 
      # prints the sum of all the even numbers in the list.

def sum_numbers():
    l = range(50,90)
    sums = 0
    for i in l:
        if 1 % 2 == 0:
             print (sums)
        else:
            print("not divisible by three")
            sums = sums+1
            print (sums)   


sum_numbers()            


#Qsn 4) Write a function that takes any two integers as input, and prints the sum 
      # of all the numbers between the two integers (inclusive) that are divisible by 3.
        
def by_three():
    num = range(10,20)
    sum_number = 0
    for n in num:
        if n % 3 == 0:
            print(sum_number)
    else:
        print("number is divisible by three")  
        sum_number= sum_number+1  
        print(sum_number)    

  
by_three()  
   
            

