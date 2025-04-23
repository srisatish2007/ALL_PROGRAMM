"""
Write a Python class Employee with attributes like emp_id, emp_name, emp_salary, 
and emp_department and methods like calculate_emp_salary, emp_assign_department, 
and print_employee_details.

Sample Employee Data:
    "ADAMS", "E7876", 50000, "ACCOUNTING"
    "JONES", "E7499", 45000, "RESEARCH"
    "MARTIN", "E7900", 50000, "SALES"
    "SMITH", "E7698", 55000, "OPERATIONS"
Use 'assign_department' method to change the department of an employee.
Use 'print_employee_details' method to print the details of an employee.
Use 'calculate_emp_salary' method takes two arguments: salary and hours_worked,
which is the number of hours worked by the employee. If the number of hours worked 
is more than 50, the method computes overtime and adds it to the salary. Overtime 
is calculated as following formula:
    overtime = hours_worked - 50
    Overtime amount = (overtime * (salary / 50))
"""


class employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department, hour_worked):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
        self.depart = emp_department
        self.hour_worked = hour_worked
        self.overtime_salary = 0

    def cal_salary(self):
        self.time = self.hour_worked
        if self.time > 50:
            self.overtime = self.time - 50
            self.overtime_salary = self.overtime * (self.salary / 50)
            self.total_sal = self.salary + self.overtime_salary

    def assign_emp_dep(self, new_dep):
        self.depart = new_dep

    def print_all_detail(self):
        print("")
        # print("                PRINTING ALL DETAILS                ")
        print("     -----------------------------------------------")
        print("\tDETAILS OF ", self.name, " : ")
        print("\v\t", "NAME         : ", self.name)
        print("\t", "ID           : ", self.id)
        print("\t", "DEPARTMENT   : ", self.depart)
        print("\t", "WORKED HOURS : ", self.hour_worked)
        print("\t", "SALARY       : ", self.salary)
        if self.overtime_salary > 0:
            print("\t", "OVER TIME SALARY : ", self.overtime_salary)
            print("\t", "TOTAL SALARY : ", self.total_sal)
        else:

            print("\t", "NO OVER TIME SALARY ")
        print("\t", "==============================================")


num = []
j = 0
n = 0


def add_emp():
    global n
    n1 = int(input("\tENTER NUMBER OF EMPLOYEE'S : "))
    global num
    global j
    for i in range(n, n1):
        st = "o" + str(i + 1)
        num.append(st)
    # print(num)

    for i in range(0, n1):
        print("\tENTER THE DETAILS OF THE EMPLOYEE", i + 1)
        print("\t===================================")
        name = input("\t  ENTER THE NAME: ")
        name1 = name.upper()
        Id = input("\t  ENTER THE ID NUMBER : ")
        sal = int(input("\t  ENTER SALARY OF THE EMPLOYEE : "))
        dep = input("\t  ENTER DEPARTMENT : ")
        dep1 = dep.upper()
        tim = int(input("\t  ENTER WORKED HOURS : "))
        print("")
        print("")
        num[i] = employee(
            emp_id=Id,
            emp_name=name1,
            emp_salary=sal,
            emp_department=dep1,
            hour_worked=tim,
        )
        num[i].cal_salary()
        n = n + n1


def find_emp():
    global num
    fin_2 = 541
    ind_fin = 540
    fin_emp_name1 = input("\v\tENTER THE NAME OF THE EMPLOYEE TO SEARCH : ")
    fin_emp_name = fin_emp_name1.upper()
    for i in range(len(num)):
        obj = num[i].name
        if obj == fin_emp_name:
            ind_fin = i
            fin_2 = i
    if ind_fin == fin_2:
        print("\t  ", fin_emp_name, "EXSIT IN THE CLASS")
        opt = input("\t   DO YOU WANT TO PRINT " + fin_emp_name + " DETAILS ")
        if opt == "yes" or "Yes" or "YES":
            num[ind_fin].print_all_detail()
        else:
            pass
    else:
        print("\tNO EMPLOYEE FOUND WITH THE GIVEN NAME " + fin_emp_name)


def pri_emp():
    global num
    fin_1_2 = 5610
    ind_pri = 5600
    pri_emp_name1 = input("\v\tENTER THE NAME OF THE EMPLOYEE TO PRINT DETAILS : ")
    pri_emp_name = pri_emp_name1.upper()
    for i in range(len(num)):
        if num[i].name == pri_emp_name:
            ind_pri = i
            fin_1_2 = i
    if ind_pri == fin_1_2:
        num[ind_pri].print_all_detail()
    else:
        print("\tNO EMPLOYEE FOUND WITH THE GIVEN NAME ", pri_emp_name)


while True:
    print(
        """\tMAIN MENU 
    \t`````````"""
    )
    print("\t  1) ADD MORE EMPLOYEES DETAILS.")
    print("\t  2) FIND EMPLOYEE WITH NAME.")
    print("\t  3) PRINT EMPLOYEE DETAIL.")
    print("\t  4) PRINT DETAILS OF ALL EMPLOYEES.")
    print("\t  5) EXIT MAIN MENU.")
    print("")
    op = int(input("\tENTER YOUR OPTION : "))
    if op == 1:
        add_emp()
    elif op == 2:
        find_emp()
    elif op == 3:
        pri_emp()
    elif op == 4:
        print("                PRINTING ALL DETAILS                ")
        print("     -----------------------------------------------")
        for j in range(0, len(num)):
            num[j].print_all_detail()
    else:
        print("PROGRAM COMPLETED SUCCESSFULLY")
