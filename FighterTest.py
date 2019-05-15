import unittest
from Character import Character
from Attack import Attack
from Fighter import Fighter


class FighterTest(unittest.TestCase):

    def test_attackRollIncreasedEveryLevel(self):
        testCharacter1 = Fighter()
        testCharacter2 = Character()
        testCharacter1.levelUp()
        testCharacter1.levelUp()
        roll = 1
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.modifyRoll()

        self.assertEqual(3, attack.modifiedRoll)

    def test_fighterGainsTenHPPerLevel(self):
        testCharacter1 = Fighter()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 990
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(20, testCharacter1.hitPoints)
