# -*- coding: utf-8 -*-


from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.exceptions import Unauthorized
from .models import User


class AuthView(HTTPMethodView):
    async def post(self, request):
        data = request.json
        user = await User.get_or_none(username=data.get("username"))

        if not user or not user.verify_password(data.get("password")):
            raise Unauthorized("Invalid credentials")

        if not user.is_active:
            raise Unauthorized("User inactive")

        return json({
            "access_token": jwt_manager.generate_token(user.id),
            "token_type": "bearer"
        })

class LogoutView(HTTPMethodView):
    async def post(self, request):
        # 实现令牌失效逻辑（需要Redis等存储）
        return json({"message": "Logout successful"})


class UserView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})


class GroupView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})


class RoleView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})


class PermissionView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})
