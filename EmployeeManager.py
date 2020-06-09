class Employee:
   
   """
   Employee Class contains firstname,lastname,ssn and salary properties
   and giveRaise method.Include also magic methods
   """
   def __init__(self, firstname, lastname, ssn, salary=0.0):
       """
        class constructor
       """
       self.firstname = firstname
       self.lastname = lastname
       self.ssn= ssn
       self.salary = salary

   def __str__(self):
       """
       class as string 
       """
       return 'First name: ' + self.firstname + '\nLast name: ' + self.lastname + '\nSocial Security Number: ' + self.ssn + '\nSalary: ' + str(self.salary) + '\n'

   def giveRaise(self, percentRaise):
       """
       give raise in salary by accepting raising percentage
       """
       self.salary = self.salary + (self.salary*percentRaise/100.0)
     
   def __lt__(self,other):
       """
       less than comparison magic method
       """
       if self.lastname.lower() < other.lastname.lower():
           return True
       elif self.lastname.lower() == other.lastname.lower():
           if self.firstname.lower() < other.firstname.lower():
               return True
           else:
               return False
       else:
           return False
       
   def __eq__(self,other):
       """
       Equal comparison magic method
       """
       if self.firstname.lower() == other.firstname.lower() and self.lastname.lower() == other.lastname.lower():
           return True
       else:
           return False





class Manager(employee.Employee):
   """
   Manager class inherits Employee. Have extra title property
   Includes constructor and string method
   """
    
    
   def __init__(self, firstname, lastname, ssn, salary, title):
       """
       class constructor. Also calls super class constructor
       """
       super().__init__(firstname, lastname, ssn, salary)
       self.title = title

   def __str__(self):
       """
       string method. Calls super class string method
       """
       super().__str__()
       return super().__str__() + 'Title: ' + self.title + '\n'
       



listOfObjects = []

# create Employee object
emp = employee.Employee('John', 'Doe', '456-22-9834', 9000)
listOfObjects.append(emp)

# create Manager object
man = manager.Manager('Jane', 'Aoe', '123-98-6665', 15000, 'Senior Manager')
listOfObjects.append(man)

emp2 = employee.Employee('vohn', 'Foe', '456-22-9834', 9000)
listOfObjects.append(emp2)

# create Manager object
man2 = manager.Manager('Zane', 'Foe', '123-98-6665', 15000, 'Senior Manager')
listOfObjects.append(man2)

listOfObjects.sort()

for p in listOfObjects:
   print ('\nBefore Raise:')
   print (p.__str__())
   p.giveRaise(5)
   print ('\nAfter giving Raise:')
   print(p.__str__())
   
print(man==emp)
print(man<emp)
print(emp<man)
