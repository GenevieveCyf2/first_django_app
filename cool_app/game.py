	

from random import randint

class StudentFighter(object):

    def __init__(self, strength, health, name):
        self.strength = strength
        self.name = name
        self.health = health


    def attack(self, opponent):
        multiplier = randint(1, 4)
        damage = multiplier * self.strength
        opponent.health -= damage

        message_one = "A successful attack!"

        if multiplier > 2:
            message_one += " Critical Damage!"

        # Lastly, let's add a message to handle
        # the situation in which our opponent has no
        # more life points

        # if opponent still has health
        # take away health points and
        # show remaining health points
        # else show opponent has fainted.
        if opponent.health > 0:
            # if opponent still has health points simply
            # show how many left
            message_two = "{} has {} health points remaining".format(opponent.name, opponent.health)
        else:
            # if opponent has none left show they have fainted.
            message_two = "{} has fainted. You win!".format(opponent.name)
        return message_one, message_two 


kalu = StudentFighter(strength=3, health=100, name="Kalu")
david = StudentFighter(strength=5, health=100, name="David")

kalu.attack(david)
