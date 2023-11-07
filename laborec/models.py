from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class POST(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    saikin_fridge1 = models.PositiveSmallIntegerField(default=5)
    saikin_fridge2 = models.PositiveSmallIntegerField(default=5)
    saikin_fridge3 = models.PositiveSmallIntegerField(default=5)
    saikin_fridge4 = models.PositiveSmallIntegerField(default=5)
    saikin_fridge5 = models.PositiveSmallIntegerField(default=5)
    saikin_feezer1 = models.IntegerField(default=-32)
    saikin_incubater1 = models.PositiveSmallIntegerField(default=35)
    saikin_incubater2 = models.PositiveSmallIntegerField(default=36)
    saikin_incubater3 = models.PositiveSmallIntegerField(default=36)
    saikin_wkprint = models. BooleanField(default=False)

    seika_fridge1 = models.PositiveSmallIntegerField(default=5)
    seika_fridge2 = models.PositiveSmallIntegerField(default=5)
    seika_fridge3 = models.PositiveSmallIntegerField(default=5)
    seika_fridge4 = models.PositiveSmallIntegerField(default=5)
    seika_fridge5 = models.PositiveSmallIntegerField(default=5)
    seika_fridge6 = models.PositiveSmallIntegerField(default=5)
    seika_fridge7 = models.PositiveSmallIntegerField(default=5)
    seika_freezer1 = models.IntegerField(default=-30)
    seika_samplecheck = models.BooleanField(default=False)

    yuketu_fridge1 = models.FloatField(default=4.0)
    yuketu_fridge2 = models.FloatField(default=4.0)
    yuketu_fridge3 = models.FloatField(default=4.0)
    yuketu_fridge4 = models.FloatField(default=5.0)
    yuketu_shake1 = models.FloatField(default=22.0)
    yuketu_freezer1 = models.IntegerField(default=-30)
    yuketu_freezer2 = models.IntegerField(default=-30)
    yuketu_visual_fridge1 = models.IntegerField(default=4)
    yuketu_visual_fridge2 = models.IntegerField(default=4)
    yuketu_visual_fridge3 = models.IntegerField(default=4)
    yuketu_visual_fridge4 = models.IntegerField(default=6)
    yuketu_visual_shake1 = models.IntegerField(default=23)
    yuketu_visual_freezer1 = models.IntegerField(default=-30)
    yuketu_visual_freezer2 = models.IntegerField(default=-30)
    yuketu_lockcheck = models.BooleanField(default=False)

    ketueki_fridge1 = models.IntegerField(default=5)
    ketueki_freezer1 = models.IntegerField(default=-80)

    recorder = models.CharField(max_length=20, default="username", null=False)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_at)