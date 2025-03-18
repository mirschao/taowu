# -*- coding: utf-8 -*-


from sanic import Blueprint
from .views import UserView, GroupView


authorization_bp = Blueprint('authorizations', url_prefix='/authorizations')

# 注册类视图
authorization_bp.add_route(UserView.as_view(), '/users')
authorization_bp.add_route(GroupView.as_view(), '/groups')
