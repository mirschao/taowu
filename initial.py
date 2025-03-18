from plugins.authorization.models import User, Group, Role, Permission


async def init_rbac():
    # 创建权限
    user_read = await Permission.create(name="user.read", description="Read user info")
    user_manage = await Permission.create(name="user.manage", description="Manage users")

    # 创建角色
    admin_role = await Role.create(name="admin")
    await admin_role.permissions.add(user_read, user_manage)

    # 创建用户组
    dev_group = await Group.create(name="developers")
    await dev_group.roles.add(admin_role)

    # 创建测试用户
    admin = await User.create(username="admin", is_active=True)
    admin.set_password("admin123")
    await admin.save()
    await admin.roles.add(admin_role)
    await admin.groups.add(dev_group)
    print("RBAC initialized")
