import unittest
from Character import Character
from Attack import Attack
from Roll import Roll


class CharacterTest(unittest.TestCase):

    def test_ifTargetCharacterHitTakesOneDamage(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(4, testCharacter2.hitPoints)

    def test_ifRollIs20CriticalHitDoubleDamage(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        roll = 20
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(3, testCharacter2.hitPoints)

    def test_ifTargetCharacterHP0OrLessTargetIsDead(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter2.hitPoints = 1
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()
        testCharacter2.checkLivingStatus()

        self.assertFalse(testCharacter2.isAlive)

    def test_DeadCharacterCannotBeAttacked(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter2.isAlive = False
        testCharacter2.hitPoints = 0
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(0, testCharacter2.hitPoints)

    def test_StrModIsAppliedToAttack(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.strength = 12
        roll = testCharacter2.armor - 1
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(3, testCharacter2.hitPoints)
    
    def test_StrModIsDoubleOnCritHit(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.strength = 12
        testCharacter2.hitPoints = 6
        roll = 20
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()
        testCharacter2.checkLivingStatus()

        self.assertFalse(testCharacter2.isAlive)

    def test_MinDmgAlwaysOne(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.strength = 1
        roll = 20
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()
        self.assertEqual(4, testCharacter2.hitPoints)

    def test_DexModIsAppliedToArmor(self):
        testCharacter1 = Character()
        testCharacter1.dexterity = 12
        testCharacter1.updateArmor()

        self.assertEqual(11, testCharacter1.armor)
    
    def test_ConstModIsAppliedToHitPoints(self):
        testCharacter1 = Character()
        testCharacter1.constitution = 12
        testCharacter1.updateHitPoints(testCharacter1.getConstitutionModifier())

        self.assertEqual(6, testCharacter1.hitPoints)

    def test_CharacterGainsTenExperienceOnSuccessful(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        roll = testCharacter2.armor + 1
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(10, testCharacter1.experiencePoints)

    def test_CharacterLevelsAfter1000ExperiencePoints(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 990
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(testCharacter1.level, 2)

    def test_CharacterOnlyLevelsEvery1000ExperiencePoints(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 1001
        testCharacter1.level = 2
        roll = testCharacter2.armor
        attack = Attack(testCharacter1, testCharacter2, roll)

        attack.attemptAttack()

        self.assertEqual(testCharacter1.level, 2)

    def test_CharacterHitPointsIncreaseOnLevelUp(self):
        testCharacter1 = Character()
        testCharacter1.levelUp()

        self.assertEqual(10, testCharacter1.hitPoints)

    def test_RollModifierOnEvenLevel(self):
        testCharacter1 = Character()
        testCharacter2 = Character()
        testCharacter1.experiencePoints = 2000
        testCharacter1.levelUp()
        testCharacter1.levelUp()
        roll = 1

        modifiedRoll = Roll(testCharacter1, testCharacter2, roll)

        modifiedRoll.modifyRoll()

        self.assertEqual(2, modifiedRoll.modifiedRoll)
