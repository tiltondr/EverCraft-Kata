from Character import Character
class Monk(Character):

    def levelUp(self):
        self.level += 1
        self.updateHitPoints(6 + self.getConstitutionModifier())