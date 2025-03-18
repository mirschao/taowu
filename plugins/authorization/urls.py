# -*- coding: utf-8 -*-


from sanic import Blueprint
from .views import AuthView, LogoutView, UserView, GroupView, RoleView, PermissionView


authorization_bp = Blueprint('authorizations', url_prefix='/authorizations')

# 注册中间件
# authorization_bp.middleware('request')(jwt_auth_middleware)
# authorization_bp.middleware('request')(rbac_middleware)

# 注册类视图
authorization_bp.add_route(AuthView.as_view(), '/login')
authorization_bp.add_route(LogoutView.as_view(), '/logout')
authorization_bp.add_route(UserView.as_view(), '/users')
authorization_bp.add_route(GroupView.as_view(), '/groups')
authorization_bp.add_route(RoleView.as_view(), '/roles')
authorization_bp.add_route(PermissionView.as_view(), '/permissions')
