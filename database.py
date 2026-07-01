import json
import os 

File="employees.json"

def load_data():
    if not os.path.exists(File):
        return[]
    with open(File,"r") as f:
        try:
            return json.load(f)
        except:
            return[]


def save_data(data):
    with open(File,"w") as f:
        json.dump(data,f,indent=4)


def add_employee(employee):
    data = load_data()
    data.append(employee)
    save_data(data)



def view_employee():
    return load_data()



def search_employee(emp_id):
    data = load_data()
    for emp in data :
        if emp["ID"] == emp_id:
            return emp
        return None
    


def delete_employee(emp_id):
    data = load_data()
    new_data =[emp for emp in data if emp["ID"] != emp_id]
    save_data(new_data)




