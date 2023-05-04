# 1) Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials

# class Student:
#     firsrt_name = "Otieno"
#     last_name ="Yekebedi"
#     age = 22
#     school = "AkiraChix"
    # Country = "Kenya"


class Student:
    school = "AkiraChix"
    def __init__(self,first_name ,last_name, age, country):
        self.first_name = first_name 
        self.last_name = last_name
        self.age = age 
        self.country= country

    def show_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def  year_of_birth(self):
        return f"{self.year_of_birth} - {self.age}"

    def show_initials(self):
        return f"{self.first_name[0]} {self.last_name[0]}"


  

        