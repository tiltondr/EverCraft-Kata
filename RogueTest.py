import unittest
from Character import Character
from Attack import Attack
from Rogue import Rogue
from Roll import Roll


class RogueTest(unittest.TestCase):

    def test_tripleDmgOnCritHit(self):
        testCharacter1 = Rogue()
        testCharacter2 = Character()
        roll = Roll(testCharacter1, testCharacter2, 20)
        attack = Attack(testCharacter1, testCharacter2, roll.initialRoll)

        attack.attemptAttack()

        self.assertEqual(2, testCharacter2.hitPoints)

    def test_ifOpponentDexModIsPositiveModIsNotAppliedToArmor(self):
        testCharacter1 = Rogue()
        testCharacter2 = Character()
        testCharacter2.dexterity = 12
        roll = 10
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()
        
        self.assertEqual(4, testCharacter2.hitPoints)

