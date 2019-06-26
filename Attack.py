from Damage import Damage
from Roll import Roll


class Attack:

    def __init__(self, attacker, defender, roll):
        self.attacker = attacker
        self.defender = defender
        self.roll = roll


    def attemptAttack(self):
        self.defender.updateHitPoints(self.defender.getConstitutionModifier())
        successfulRoll = Roll(self.attacker, self.defender, self.roll).isSuccessful()
        
        if successfulRoll:
            Damage(self.attacker, self.defender, self.roll).applyDamage()
            self.attacker.updateCharacter()

    

