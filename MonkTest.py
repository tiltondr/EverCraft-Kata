import unittest
from Character import Character
from Attack import Attack
from Monk import Monk
from Roll import Roll


class MonkTest(unittest.TestCase):

    def test_monkGains6HPPerLevel(self):
        testCharacter1 = Monk()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 990
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(11, testCharacter1.hitPoints)