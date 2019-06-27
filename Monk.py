from Character import Character
from math import floor
class Monk(Character):

    def levelUp(self):
        self.level += 1
        self.updateHitPoints(6 + self.getConstitutionModifier())

    def getModifiedArmor(self):
        return self.armor + self.getDexterityModifier() + max(self.getWisdomModifier(),0)

    def getRollModifier(self):
        levelMod = 1 if self.level % 3 != 1 else 0
        return self.getStrengthModifier() + floor(self.level / 2) + levelMod