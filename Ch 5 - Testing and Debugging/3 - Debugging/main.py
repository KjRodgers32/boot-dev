def take_magic_damage(health, resist, amp, spell_power):
    total_damage = amp * spell_power
    actual_damage_dealt = total_damage - resist
    new_health = health - actual_damage_dealt
    return new_health