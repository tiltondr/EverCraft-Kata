import unittest
from Character import Character
from Attack import Attack
from Fighter import Fighter
from Roll import Roll


class FighterTest(unittest.TestCase):

    def test_attackRollIncreasedEveryLevel(self):
        testCharacter1 = Fighter()
        testCharacter2 = Character()
        testCharacter1.levelUp()
        testCharacter1.levelUp()
        roll = Roll(testCharacter1, testCharacter2, 1)

        roll.modifyRoll()

        self.assertEqual(3, roll.modifiedRoll)

    def test_fighterGainsTenHPPerLevel(self):
        testCharacter1 = Fighter()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 990
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(20, testCharacter1.hitPoints)
