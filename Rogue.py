from Character import Character
from math import floor

class Rogue(Character):
    
    def calculateStrengthModifier(self, initialRoll):
        return 2 * self.getDexterityModifier() if initialRoll == 20 else self.getDexterityModifier()

    def getRollModifier(self):
        return self.getDexterityModifier() + floor(self.level / 2)