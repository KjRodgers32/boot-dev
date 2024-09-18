from Wizard import Wizard

test_cases = [
    ('Kevin', 100, 100, 'Kevin',10000, 1000, 9500, 1100),
    ('Taylor', 65, 94, 'Taylor',6500, 940, 6000, 1040),
    ('Reggie', 57, 47, 'Reggie',5700, 470, 5200, 570),
    ('Tyson', 99, 89, 'Tyson',9900, 890, 9400, 990),
]

def test(name, stamina, intelligence, expected_name, expected_health, expected_mana, expected_new_health, expected_new_mana):
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

    print("Gets fireballed!")
    wizard.get_fireballed()
    print(f"Expected New Health: {expected_new_health}")
    print(f"Actual New Health: {wizard.health}")

    if expected_new_health != wizard.health:
        print('Fail')
        return False
    
    print("Drinks Mana Potion!")
    wizard.drink_mana_potion()
    print(f"Expected New Mana: {expected_new_mana}")
    print(f"Actual New Health: {wizard.mana}")

    if expected_new_mana!= wizard.mana:
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
