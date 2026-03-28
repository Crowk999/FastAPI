from tortoise import models, fields
from enum import IntEnum

class AgeEnum(IntEnum):
    CHILD = 0
    TEEN = 1
    ADULT = 2
    SENIOR = 3

class user(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length = 100)
    age = fields.IntEnumField(AgeEnum)

    def __str__(self):
        return self.name