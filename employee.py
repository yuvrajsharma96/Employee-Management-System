class Employee:
    def __init__(self,name,salary,empid,age,department):
        name =self.name
        empid =self.empid
        age = self.age
        department = self.department
        salary = self.salary
    def to_dict(self):
        return{
            "ID": self.empid,
            "Name": self.name,
            "Age": self.age,
            "Salary": self.salary,
            "Department": self.department
        }


