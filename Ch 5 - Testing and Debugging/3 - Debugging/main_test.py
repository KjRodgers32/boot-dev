from main import *

run_cases = [
    (1000,45,25,10,795),
    (900,83,38,20,223),
    (750,10,50,50,-1740)
]

def test(input1, input2, input3, input4, expected_result):
    print("---------------------------------")
    print(f"Input: {input1}, {input2}, {input3}, {input4}")
    print(f"Expecting: {expected_result}")
    result = take_magic_damage(input1, input2, input3, input4)
    print(f"Acutal: {result}")

    if result == expected_result:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    
    for test_case in run_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

main()
