from abc import ABC, abstractmethod


class SalaryReportVisitor(ABC):

    @abstractmethod
    def visit_company(self, company): pass

    @abstractmethod
    def visit_department(self, department): pass

    @abstractmethod
    def visit_employee(self, employee): pass



class Element(ABC):
    @abstractmethod
    def accept(self, visitor: SalaryReportVisitor):
        pass


class Employee(Element):
    def __init__(self, position: str, salary: float):
        self.position = position
        self.salary = salary

    def accept(self, visitor: SalaryReportVisitor):
        return visitor.visit_employee(self)


class Department(Element):
    def __init__(self, employees: list):
        self.employees = employees

    def accept(self, visitor: SalaryReportVisitor):
        return visitor.visit_department(self)


class Company(Element):
    def __init__(self, departments: list):
        self.departments = departments

    def accept(self, visitor: SalaryReportVisitor):
        return visitor.visit_company(self)


class SalaryReportGenerator(SalaryReportVisitor):

    def visit_company(self, company: Company):
        total = 0
        lines = ["--- Salary Report for Company ---"]
        for department in company.departments:
            dept_result = department.accept(self)
            lines.append(dept_result["text"])
            total += dept_result["sum"]
        lines.append(f"TOTAL COMPANY PAYROLL: {total}")
        return {"sum": total, "text": "\n".join(lines)}

    def visit_department(self, department: Department):
        total = 0
        lines = ["--- Department ---"]
        for emp in department.employees:
            emp_result = emp.accept(self)
            lines.append(emp_result["text"])
            total += emp_result["sum"]
        lines.append(f"DEPARTMENT TOTAL: {total}")
        return {"sum": total, "text": "\n".join(lines)}

    def visit_employee(self, employee: Employee):
        return {"sum": employee.salary, "text": f"{employee.position}: {employee.salary}"}


if __name__ == "__main__":
    # створюємо елементи
    dep1 = Department([
        Employee("Developer", 3000),
        Employee("QA", 2000)
    ])

    dep2 = Department([
        Employee("Manager", 4000),
        Employee("Designer", 2500)
    ])

    company = Company([dep1, dep2])

    visitor = SalaryReportGenerator()
    company_report = company.accept(visitor)
    print(company_report["text"])
    dep_report = dep1.accept(visitor)
    print(dep_report["text"])
