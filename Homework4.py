num_employees = int(input("Кількість працівників: "))
employees = []

for i in range(num_employees):
    employee = {}
    employee['name'] = input(f"Імя працівника {i + 1}: ")

    while True:
        employee_id = input("ID працівника: ")
        if not any(emp.get('id') == employee_id for emp in employees):
            employee['id'] = employee_id
            break
        else:
            print("ID не унікальний.")

    employees.append(employee)

print("Результат:")
print(employees)
