fruitcompanies = [{"name": "Zesty", "employees": ["Ambu", "Brent", "Bryan", "Carlee", "Chad"]},
                  {"name": "Ripe.ly", "employees": ["Darlene", "Eric", "Fernando", "Peter", ]},
                  {"name": "FruitBee", "employees": ["Jennae", "Joel", "Jonas", "Josh", ]},
                  {"name": "JuiceGrove", "employees": ["Kurt", "Nate", "Patrick", "Rachel", ]}]

terminated_employees = ['Chad']


def get_user_input():
    user_input = input("Enter the name of an company: ")
    return user_input


# Satisfies Function 1 requirements
def list_employees(companies: dict = [], match='Joel'):
    # loop through each company
    key = 'employees'
    for company in companies:
        # check if the employee is part of the company
        if match in company[key]:
            print(f"{company['name']} Employees: ")
            for employee in company[key]:
                print(employee)
            print("\n\n\n")


def list_employees_by_company_name(companies: dict = [], match=''):
    # loop through each company
    key = 'name'
    for company in companies:
        # check if the employee is part of the company
        if match in company[key]:
            print(f"{company['name']} Employees: ")
            for employee in company['employees']:
                print(employee)
            print("\n\n\n")


def list_active_employees_by_company_name(companies: dict = [], match='', fired_employees=[]):
    # loop through each company
    key = 'name'
    for company in companies:
        # check if the employee is part of the company
        if match in company[key]:
            print(f"{company['name']} Employees: ")
            for employee in company['employees']:
                if len(fired_employees) > 0 and employee not in fired_employees:
                    print(employee)
            print("\n\n\n")


def main():
    # Call Function 1
    list_employees(fruitcompanies)

    # Call Function 2
    list_employees_by_company_name(fruitcompanies, get_user_input())

    # Call Function 3
    list_active_employees_by_company_name(fruitcompanies, get_user_input(), terminated_employees)


if __name__ == "__main__":
    main()
