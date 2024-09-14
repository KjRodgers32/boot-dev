from Employee import Employee

test_cases = [
    ("Kevin", "Rodgers", 1, "DA", 75000, "Kevin Rodgers", 1),
    ("Taylor", "Rodgers", 2, "SWE", 100000, "Taylor Rodgers", 2),
    ("Reggie", "Rodgers", 3, "SWM", 120000, "Reggie Rodgers", 3),
]

def test(first_name, last_name, id, position, salary, expected_name, expected_employees):
    print("------------------------------")
    employee = Employee(first_name, last_name, id, position, salary)
    print("Testing Employee")

    name = employee.get_name()
    print(f"Expected name: {expected_name}")
    print(f"Actual name: {name}")

    print(f"Expected employee count: {expected_employees}")
    print(f"Actual employee count: {Employee.total_employees}")

    if name != expected_name or Employee.total_employees != expected_employees:
        print("Fail")
        return False
    print("Pass")
    return True

def main():
    passed = 0
    failed = 0
    for tc in test_cases:
        correct = test(*tc)

        if correct:
            passed += 1
        else:
            failed += 1
    print("----------------------------")


    if failed > 0:
        print("========== Failed ==========")
    else:
        print("========== Passed ==========")

    print(f"Passed: {passed} Failed: {failed}")
main()