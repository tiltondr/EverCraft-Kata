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

    def test_does3DmgInsteadOf1OnSuccessfulAttack(self):
        testCharacter1 = Monk()
        testCharacter2 = Character()
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(2, testCharacter2.hitPoints)

    def test_addWisdomModIfPositiveToArmor(self):
        testCharacter1 = Character()
        testCharacter2 = Monk()
        testCharacter2.wisdom = 12
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(5, testCharacter2.hitPoints)

    def test_dontAddWisdomModIfNegativeToArmor(self):
        testCharacter1 = Character()
        testCharacter2 = Monk()
        testCharacter2.wisdom = 8
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(4, testCharacter2.hitPoints)

    def test_attackRollIncreasedBy1Every2ndLevel(self):
        testCharacter1 = Monk()
        testCharacter2 = Character()
        testCharacter1.level = 2
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor-1)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(2, testCharacter2.hitPoints)

    def test_attackRollIncreasedBy1Every3rdLevel(self):
        testCharacter1 = Monk()
        testCharacter2 = Character()
        testCharacter1.level = 3
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor-1)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(2, testCharacter2.hitPoints)

    def test_attackRollNotIncreasedIfNot2ndOr3rdLevel(self):
        testCharacter1 = Monk()
        testCharacter2 = Character()
        roll = Roll(testCharacter1, testCharacter2, testCharacter2.armor-1)

        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(5, testCharacter2.hitPoints)