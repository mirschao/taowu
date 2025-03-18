# -*- coding: utf-8 -*-


from sanic import Sanic
from sanic.log import logger
from tortoise import Tortoise
from tortoise.contrib.sanic import register_tortoise
from settings import MyConfig
from plugins.authorization.urls import authorization_bp


app = Sanic(__name__, log_config=MyConfig.LOGGING_CONFIG_DEFAULTS)
app.update_config(MyConfig)

# 注册蓝图
app.blueprint(authorization_bp)

# 初始化Tortoise ORM
register_tortoise(
    app, db_url="sqlite://db.sqlite3",
    modules={
        "models": [
            "plugins.authorization.models",
            # "plugins.auditlog.models",
            # "plugins.workflow.models"
        ]
    },
    generate_schemas=True
)

@app.after_server_stop
async def close_db(app, _):
    await Tortoise.close_connections()
    logger.info("Tortoise connection closed")


if __name__ == "__main__":
    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG
    )
