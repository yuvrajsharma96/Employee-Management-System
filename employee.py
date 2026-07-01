class Employee:
    def __init__(self,name,salary,empid,age,department):
        self.name = name 
        self.empid = empid 
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


