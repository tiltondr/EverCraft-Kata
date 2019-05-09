class Attack:

    def __init__(self, attacker, defender, initialRoll):
        self.attacker = attacker
        self.defender = defender
        self.initialRoll = initialRoll
        self.modifiedRoll = initialRoll

    def attemptAttack(self):
        self.modifyRoll()
        self.defender.updateHitPoints(self.defender.getConstitutionModifier())
        if self.modifiedRoll >= self.defender.armor and self.defender.isAlive:
            self.dealDamage(self.calculateDamage())
            self.attacker.updateCharacter()

    def modifyRoll(self):
        self.modifiedRoll = self.initialRoll + self.attacker.getRollModifier()

    def calculateDamage(self):
        damage = 0
        if self.initialRoll == 20:
            damage = self.calculateCritDamage()
        else:
            damage = self.calculateStandardDamage()
        return max(damage, 1)

    def calculateCritDamage(self):
            return 2 * self.calculateStandardDamage()

    def calculateStandardDamage(self):
            return 1 + self.calculateStrengthModifier()

    def calculateStrengthModifier(self):
            return 2 * self.attacker.getStrengthModifier() if self.initialRoll == 20 else self.attacker.getStrengthModifier()

    def dealDamage(self, damage):
        self.defender.updateHitPoints(-damage)

    
    
    

    

    
