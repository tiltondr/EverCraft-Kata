from math import floor

class Character:

    abilityMods = {
        1: -5,
        2: -4,
        3: -4,
        4: -3,
        5: -3,
        6: -2,
        7: -2,
        8: -1,
        9: -1,
        10: 0,
        11: 0,
        12: 1,
        13: 1,
        14: 2,
        15: 2,
        16: 3,
        17: 3,
        18: 4,
        19: 4,
        20: 5
    }

    def __init__(self):
        self.armor = 10
        self.hitPoints = 5
        self.isAlive = True
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.experiencePoints = 0
        self.level = 1

    def getStrengthModifier(self):
        return self.abilityMods[self.strength]

    def getDexterityModifier(self):
        return self.abilityMods[self.dexterity]

    def getConstitutionModifier(self):
        return self.abilityMods[self.constitution]

    def getRollModifier(self):
        return self.getStrengthModifier() + floor(self.level / 2)

    def updateArmor(self):
        self.armor += self.getDexterityModifier()

    def updateHitPoints(self, amount):
        self.hitPoints += amount
    
    def checkLivingStatus(self):
        if(self.hitPoints <= 0 and self.isAlive):
            self.updateLivingStatus()

    def updateLivingStatus(self):
        self.isAlive = False

    def updateExperiencePoints(self):
        currentExperiencePoints = self.experiencePoints
        self.experiencePoints += 10

        self.checkLevelUp(currentExperiencePoints)

    def checkLevelUp(self, previousExperiencePoints):
        if previousExperiencePoints % 1000 > 9 and self.experiencePoints % 1000 <= 9:
            self.levelUp()
        
    def levelUp(self):
        self.level += 1
        self.updateHitPoints(5 + self.getConstitutionModifier())

    def updateCharacter(self):
        self.updateExperiencePoints()
