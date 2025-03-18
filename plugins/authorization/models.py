# -*- coding: utf-8 -*-


from tortoise.models import Model
from tortoise import fields


class User(Model):
    username = fields.CharField(max_length=50, unique=True)
    password = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    groups = fields.ManyToManyField("models.Group")


class Group(Model):
    name = fields.CharField(max_length=50, unique=True)
    roles = fields.ManyToManyField("models.Role")
