# -*- coding: utf-8 -*-


from tortoise.models import Model
from tortoise import fields
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Model):
    username = fields.CharField(max_length=50, unique=True)
    password_hash = fields.CharField(max_length=128, null=True)
    is_active = fields.BooleanField(default=True)
    groups = fields.ManyToManyField("models.Group")
    roles = fields.ManyToManyField("models.Role")

    def set_password(self, password):
        self.password_hash = pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    async def get_all_permissions(self):
        # 获取直接关联的角色
        await self.fetch_related("roles__permissions")
        # 获取通过组关联的角色
        await self.fetch_related("groups__roles__permissions")

        permissions = set()
        # 直接角色权限
        for role in self.roles:
            permissions.update({perm.name for perm in role.permissions})
        # 组角色权限
        for group in self.groups:
            for role in group.roles:
                permissions.update({perm.name for perm in role.permissions})
        return list(permissions)

class Group(Model):
    name = fields.CharField(max_length=50, unique=True)
    roles = fields.ManyToManyField("models.Role")

class Role(Model):
    name = fields.CharField(max_length=50, unique=True)
    permissions = fields.ManyToManyField("models.Permission")

class Permission(Model):
    name = fields.CharField(max_length=50, unique=True)
    description = fields.TextField()