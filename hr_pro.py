class Employee:
    def __init__(self,name, age, salary, employment_year):
     self.name = name
     self.age  = age
     self.salary = salary
     self.employment_year = employment_year
    
    def get_working_years(self):
        today = 2020
        return  today - int(self.employment_year)

    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d" % (self.name,self.age,self.salary,self.get_working_years())

class Manager(Employee):
    def __init__(self, name, age,salary, employment_year,  bouns_percentage ):
        super().__init__(name, age,salary, employment_year)
        self.bouns_percentage = bouns_percentage

    def get_bonus(self):
        return self.bouns_percentage * self.salary

    def __str__(self):
        return "Name: %s, Age: %d, Salary: %d, Working Years: %d, Bonus: %f" % (self.name,self.age,self.salary,self.get_working_years(),self.get_bonus())

employees =[]
managers = []

def options():
    print()
    print("""1. Show Employees
2. Show Managers
3. Add Employee
4. Add Manager
5. Exit""")
    print()

options()
option= int(input("what would you like to do" ))


while option != 5 :
    if option== 1:
        for employee in employees:
            print (employee)
        options()
        option= int(input("what would you like to do"))    
    elif option == 2:
        for manager in managers:
            print(manager) 
        options()
        option= int(input("what would you like to do"))
    elif option == 3:
        name = input("Name: ")  
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment =  int(input("Employment Year: "))
        employee =  Employee(name,age,salary,employment)
        employees.append(employee)
        options()
        option= int(input("what would you like to do"))
    elif option == 4:
        name = input("Name: ")  
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        employment =  int(input("Employment Year: "))
        bonus =  float(input("Bonus Percentage: "))
        manager =  Manager(name,age,salary,employment, bonus)
        managers.append(manager)
        options()
        option= int(input("what would you like to do"))
    
        








    

