employee_list = []

def add_employee():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    job_title = input("Enter the job title: ")
    department = input("Enter the department: ")
    
    employee = {
        "First Name": first_name,
        "Last Name": last_name,
        "Job Title": job_title,
        "Department": department
    }
    
    employee_list.append(employee)
    print("New employee added!")

def edit_employee():
    first_name = input("Enter the first name of the employee you want to edit: ")
    last_name = input("Enter the last name of the employee you want to edit: ")
    
    for employee in employee_list:
        if employee["First Name"] == first_name and employee["Last Name"] == last_name:
            print("Employee found:")
            print(employee)
            
            new_job_title = input("Enter the new job title: ")
            new_department = input("Enter the new department: ")
            
            employee["Job Title"] = new_job_title
            employee["Department"] = new_department
            
            print("Employee updated!")
            return
    
    print("Employee with the specified name was not found.")

def delete_employee():
    first_name = input("Enter the first name of the employee you want to delete: ")
    last_name = input("Enter the last name of the employee you want to delete: ")
    
    for employee in employee_list:
        if employee["First Name"] == first_name and employee["Last Name"] == last_name:
            employee_list.remove(employee)
            print("Employee deleted!")
            return
    
    print("Employee with the specified name was not found.")

def list_employees():
    if not employee_list:
        print("No employees are registered.")
    else:
        for employee in employee_list:
            print("First Name:", employee["First Name"])
            print("Last Name:", employee["Last Name"])
            print("Job Title:", employee["Job Title"])
            print("Department:", employee["Department"])
            print()

while True:
    print("\nSelect an action:")
    print("1. Add a new employee")
    print("2. Edit an employee")
    print("3. Delete an employee")
    print("4. List all employees")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        edit_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        list_employees()
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")
