from Character import Character
from Rogue import Rogue
from Fighter import Fighter
from Monk import Monk
from Paladin import Paladin
from random import randint


class Roll:

    def __init__(self, attacker, defender, initialRoll = randint(1, 20)):
        self.attacker = attacker
        self.defender = defender
        self.initialRoll = initialRoll
        self.modifiedRoll = 0


    def modifyRoll(self):
            self.modifiedRoll = self.initialRoll + self.attacker.getRollModifier()

    def isSuccessful(self):
        self.modifyRoll()

        #TODO Clean This Up
        if self.modifiedRoll >= self.defender.getModifiedArmor() and self.defender.isAlive and not isinstance(self.attacker, Rogue):
            return True
        elif self.modifiedRoll >= self.defender.armor and self.defender.isAlive:
            return True
        else:
            return False
