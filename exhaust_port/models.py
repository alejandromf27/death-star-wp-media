from django.contrib.auth.models import User
from django.db import models


class XWing(models.Model):
    pilot = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wing')
    health = models.IntegerField(default=100, help_text="between 0 and 100")
    cost = models.FloatField(help_text="Cost in US $")
    name = models.CharField(max_length=12000)
    _coordinates = models.CharField(max_length=10000)

    def destroy(self):
        while self.health > 0:
            self.health -= 1
            self.save()

    def set_name(self, new_name):  # PEP8 python code standard recommend use variables names in snake case
        self.name = new_name

    def get_name(self):
        return self.name

    def is_destroyed(self, damage):
        return self.health - damage == 0

    def set_coordinates(self, x, y, z):
        coordinates = f"{x}0{y}0{z}"
        self._coordinates = coordinates

    def get_coordinates(self):
        coordinates = self._coordinates.split("0")
        if len(coordinates) == 3:
            x, y, z = coordinates
            return int(x), int(y), int(z)
        else:
            return None, None, None

    def __str__(self):
        return self.name


SECTORS = (("a1", 1), ("a2", 2), ("b1", 3), ("b2", 4))


class DefenceTower(models.Model):
    sector = models.CharField(max_length=1000, choices=SECTORS)
    health = models.IntegerField(default=100)
    cost = models.FloatField(help_text="Cost in US $")
    _coordinates = models.CharField(max_length=10000)
    target = models.ForeignKey('exhaust_port.XWing', on_delete=models.SET_NULL, null=True, related_name='towers')

    def is_destroyed(self, damage):
        return self.health - damage == 0

    def destroy(self):
        # this is fine to destroy tower point by point, but it take time according to the tower health
        # maybe the destroy function need to work automatically health = 0, and other function apply_damage decrease
        # the tower health in a specific damage
        # if tower is destroyed, reset the wing on target

        self.health = 0
        self.target = None
        self.save()

        # while self.health > 0:
        #     self.health -= 1  # if health if so big ex: 999 999 999 it will take a lot of time and memory
        #     self.save()

    def set_coordinates(self, x, y, z):
        coordinates = f"{x}0{y}0{z}"
        self._coordinates = coordinates

    def get_coordinates(self):
        coordinates = self._coordinates.split("0")
        if len(coordinates) == 3:
            x, y, z = coordinates
            return int(x), int(y), int(z)
        else:
            return None, None, None

    def __str__(self):
        return (self.target.name if self.target else "Without target") + ' - ' + str(dict(SECTORS)[self.sector])
