from employee import Employee
import database


def menu():
    print("\n -------Employee Management System---------")
    print("1. to add employee")
    print("2. to view employee")
    print("3. to search employee")
    print("4. to delet employee")
    print("5. Exit")



while True :
    menu()

    choice = input("enter your choice")

    if choice == "1":
        emp_id = input("enter employee ID: ")
        name = input("enter employee name: ")
        age = input ("enter employee age: ")
        department = input ("enter employee department: ")
        salary = input ("enter employee salary: ")
        
        emp = Employee(emp_id,name,age,department,salary)

        database.add_employee(emp.to_dict())

        print ("employee added sucessfully")

    elif choice == "2":
        employees = database.view_employee()

        if not employees :
            print("no employee found ")
        else: 
            for emp in employees:
             print("-------------")
             for key , value in emp.items():
                 print(f"{key}: {value}")


