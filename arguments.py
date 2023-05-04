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
          
            

