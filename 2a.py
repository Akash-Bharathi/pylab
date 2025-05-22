class Employee: 
    def __init__(self, name, employee_id, salary): 
        self.name = name 
        self.employee_id = employee_id 
        self.salary = salary 
class Salary(Employee): 
    def __init__(self, name, employee_id, salary): 
        super().__init__(name, employee_id, salary) 
    def calculate_salary(self): 
        return self.salary 
class Payroll: 
    def generate_pay_slip(self, employee): 
        print("Pay Slip:") 
        print(f"Name: {employee.name}") 
        print(f"Employee ID: {employee.employee_id}") 
        print(f"Salary: ${employee.salary}") 
        print("=" * 20) 
# Sample usage 
employee1 = Salary("John Doe", 1001, 5000) 
employee2 = Salary("Jane Smith", 1002, 6000) 
payroll = Payroll() 
payroll.generate_pay_slip(employee1) 
payroll.generate_pay_slip(employee2)