
class Character:

    def __init__(self, name=None):
        self.is_alive = True
        self.name = name if name is not None else "Stranger"
        self.health = 5
        self.armor = 10

    def attack(self, target_character, roll):
        self._apply_standard_hit_damage(roll, target_character)
        self._apply_critical_hit_damage(roll, target_character)
        target_character._update_is_alive()

    def _apply_standard_hit_damage(self, roll, target_character):
        if roll >= target_character.armor:
            target_character.health -= 1

    def _apply_critical_hit_damage(self, roll, target_character):
        if roll == 20:
            target_character.health -= 1

    def _update_is_alive(self):
        if self.health <= 0:
            self.is_alive = False