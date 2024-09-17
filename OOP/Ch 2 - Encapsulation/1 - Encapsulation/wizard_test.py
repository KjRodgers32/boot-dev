from Wizard import Wizard

test_cases = [
    ('Kevin', 100, 100, 'Kevin',10000, 1000),
    ('Taylor', 65, 94, 'Taylor',6500, 940),
    ('Reggie', 57, 47, 'Reggie',5700, 470),
    ('Tyson', 99, 89, 'Tyson',9900, 890),
]

def test(name, stamina, intelligence, expected_name, expected_health, expected_mana):
    print("--------------------")
    wizard = Wizard(name, stamina, intelligence)
    print(f"Expected name: {expected_name}")
    print(f"Actual name: {wizard.name}")

    if expected_name != wizard.name:
        print('Fail')
        return False 

    print(f"Expected health: {expected_health}")
    print(f"Actual health: {wizard.health}")

    if expected_health != wizard.health:
        print('Fail')
        return False 

    print(f"Expected mana: {expected_mana}")
    print(f"Actual mana: {wizard.mana}")

    if expected_mana != wizard.mana:
        print('Fail')
        return False 

    print('Pass')
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
    if failed > 0:
        print("========== FAILED ==========")
    else:
        print("========== PASSED ==========")
    print(f"Passed: {passed}, Failed: {failed}")

main()
