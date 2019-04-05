from django.db import models


class Pokemon(models.Model):
    row = models.DecimalField(max_digits=5, decimal_places=0)
    name = models.CharField(max_length=50)
    pokedex_Number = models.DecimalField(max_digits=5, decimal_places=0)
    img_Name = models.ImageField
    generation = models.DecimalField(max_digits=2, decimal_places=0)
    evolution_stage = models.DecimalField(max_digits=2, decimal_places=0)
    evolved = models.DecimalField(max_digits=2, decimal_places=0)
    family_Id = models.DecimalField(max_digits=2, decimal_places=0)
    cross_Gen = models.DecimalField(max_digits=2, decimal_places=0)
    Type_1 = models.CharField(max_length=50)
    Type_2 = models.CharField(max_length=50)
    weather_1 = models.CharField(max_length=100)
    weather_2 = models.CharField(max_length=100)
    state_Total = models.DecimalField(max_digits=5, decimal_places=0)
    ATK = models.DecimalField(max_digits=5, decimal_places=0)
    DEF = models.DecimalField(max_digits=5, decimal_places=0)
    STA = models.DecimalField(max_digits=5, decimal_places=0)
    legendary = models.DecimalField(max_digits=5, decimal_places=0)
    aquireable = models.DecimalField(max_digits=5, decimal_places=0)
    spawns = models.DecimalField(max_digits=5, decimal_places=0)
    regional = models.DecimalField(max_digits=5, decimal_places=0)
    raidable = models.DecimalField(max_digits=5, decimal_places=0)
    hatchable = models.DecimalField(max_digits=5, decimal_places=0)
    shiny = models.DecimalField(max_digits=5, decimal_places=0)
    nest = models.DecimalField(max_digits=5, decimal_places=0)
    new = models.DecimalField(max_digits=5, decimal_places=0)
    not_Gettable = models.DecimalField(max_digits=5, decimal_places=0)
    future_Evolve = models.DecimalField(max_digits=5, decimal_places=0)   

    def __str__(self):
        return self.row

