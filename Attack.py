from Damage import Damage
from Roll import Roll


class Attack:

    def __init__(self, attacker, defender, initialRoll):
        self.attacker = attacker
        self.defender = defender
        self.initialRoll = initialRoll


    def attemptAttack(self):
        self.defender.updateHitPoints(self.defender.getConstitutionModifier())
        successfulRoll = Roll(self.attacker, self.defender, self.initialRoll).isSuccessful()
        
        if successfulRoll:
            Damage(self.attacker, self.defender, self.initialRoll).applyDamage()
            self.attacker.updateCharacter()

    

