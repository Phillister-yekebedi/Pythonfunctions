def year_of_birth(name, age):
    year = 2023-age
    print (f"hello {name},you were born in {year}")

def my_country(country="Kenya"):
        print(f"hello you are from{country}")
        
def hello(*names):
        for name in names:
            print(f"hello {name}")

def sum(*nums):
    answer = 0
    for num in nums:
        answer += num
    return answer 

def multiply_many(**kwargs):
     answer=1
     for num in kwargs.value(): 
        answer*=num
     return answer

def concatenate_args(*students):
     name=""
     for student in students:
          name+=student
          return name
     
def concatenate_kwargs(**kwargs):
    name=""
    for student in kwargs.values():
     name+=student
    return name

def sum_multiplication(sum,multiplication):
     return(f"the sum of 6 and 2 is {sum} and their product is {multiplication}")
print(sum_multiplication(6+2,6*2) )


#default  arguments
def names(firstname="a", secondname= "b"):
     return(f"my name is {firstname} {secondname}")
print(names())
print(names(firstname="Yekebedi"))
print(names(firstname="Boss",secondname="Otieno"))

#kwargs
# def allNames(*na
    
#          final=[name for name in names]

#          print(f"hello {final}")
         
#      allNames("dad","mom","sister","brother","family")
            

