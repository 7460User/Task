class Employee:
    def __init__(self, name, employee_id, title, department):
        self.name = name
        self.employee_id = employee_id
        self.title = title
        self.department = department

    def display_details(self):
        print(f"Name: {self.name}, ID: {self.employee_id}, Title: {self.title}, Department: {self.department}")

    def __str__(self):
        return f"{self.name} - ID: {self.employee_id}"
    

    
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee_id):
        self.employees = [emp for emp in self.employees if emp.employee_id != employee_id]

    def list_employees(self):
        for employee in self.employees:
            print(employee)


            
class Company:
    def __init__(self):
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        if department_name in self.departments:
            del self.departments[department_name]

    def display_all_departments(self):
        for department in self.departments.values():
            print(f"Department: {department.name}")
            department.list_employees()
            print()

def print_menu():
    print("\nEmployee Management System Menu:")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Add Department")
    print("4. Remove Department")
    print("5. Display All Departments")
    print("6. Exit")

if __name__ == "__main__":
    company = Company()

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
   
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            title = input("Enter employee title: ")
            department_name = input("Enter employee department: ")

   
            if department_name in company.departments:
                department = company.departments[department_name]
                employee = Employee(name, employee_id, title, department_name)

          
                department.add_employee(employee)
            else:
                print(f"Error: Department '{department_name}' does not exist.")

        elif choice == "2":
     
            employee_id = input("Enter employee ID to remove: ")


            for department in company.departments.values():
                department.remove_employee(employee_id)

        elif choice == "3":
           
            department_name = input("Enter department name: ")
            department = Department(department_name)

           
            company.add_department(department)

        elif choice == "4":
            
            department_name = input("Enter department name to remove: ")

          
            company.remove_department(department_name)

        elif choice == "5":
            company.display_all_departments()

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
