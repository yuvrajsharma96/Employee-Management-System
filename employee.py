class Employee:
    def __init__(self,empid,name,age,department,salary):
        self.empid = empid
        self.name = name 
        self.age = age
        self.department = department
        self.salary =salary
        
    def to_dict(self):
        return{
            "ID": self.empid,
            "Name": self.name,
            "Age": self.age,
            "Salary": self.salary,
            "Department": self.department
        }


