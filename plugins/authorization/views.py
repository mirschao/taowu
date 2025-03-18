# -*- coding: utf-8 -*-


from sanic.views import HTTPMethodView
from sanic.response import json
from sanic.exceptions import Unauthorized
from .models import User, Group


class UserView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})

    async def post(self, request):
        return json({"hello": "world"})

    async def put(self, request):
        return json({"hello": "world"})

    async def delete(self, request):
        return json({"hello": "world"})


class GroupView(HTTPMethodView):
    async def get(self, request):
        return json({"hello": "world"})

    async def post(self, request):
        return json({"hello": "world"})

    async def put(self, request):
        return json({"hello": "world"})

    async def delete(self, request):
        return json({"hello": "world"})
