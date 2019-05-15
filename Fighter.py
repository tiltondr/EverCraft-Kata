from Character import Character
class Fighter(Character):
    
    def __init__(self):
        self.armor = 10
        self.hitPoints = 10
        self.isAlive = True
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.experiencePoints = 0
        self.level = 1

    def getRollModifier(self):
        return self.getStrengthModifier() + self.level - 1

    def levelUp(self):
        self.level += 1
        self.updateHitPoints(10 + self.getConstitutionModifier())