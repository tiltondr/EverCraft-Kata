from Rogue import Rogue
from Monk import Monk

class Damage:

    def __init__(self, attacker, defender, roll):
        self.attacker = attacker
        self.defender = defender
        self.initialRoll = roll

    def applyDamage(self):
        damage = self.calculateDamage()
        self.dealDamage(damage)

    def calculateDamage(self):
        if self.initialRoll == 20:
            damage = self.calculateCritDamage()
        else:
            damage = self.calculateStandardDamage()
        return max(damage, 1)

    def calculateCritDamage(self):
        if isinstance(self.attacker, Rogue):
            return 3 * self.calculateStandardDamage()
        else:
            return 2 * self.calculateStandardDamage()

    def calculateStandardDamage(self):
        if isinstance(self.attacker, Monk):
            return 3 + self.attacker.calculateStrengthModifier(self.initialRoll)
        return 1 + self.attacker.calculateStrengthModifier(self.initialRoll)

    def dealDamage(self, damage):
        self.defender.updateHitPoints(-damage)
